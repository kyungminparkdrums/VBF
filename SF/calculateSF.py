import sys
import os
from math import sqrt

'''
Usage:
1. Make sure you have cutflow output txt file from Plotter whose name specifies CR1 or CR2
2. Run the code by 
python3 scaleFactor.py <cutflow txt file> <bg: 'W+Jets' or 'DY+Jets'>
i.e, python3 scaleFactor.py Cutflow_from_Plotter/cutflow_2016_Z_CR1.txt DY
3. Scale factor for following steps will be printed
CR1) Trigger, Muon Selection, MET, Lepton Veto(after Tau veto), BJet Veto
CR2) Trigger, Muon Selection, MET, VBF Cuts, Lepton Veto(after Tau Veto), BJet Veto
4. Scale factor from the CR (after BJet Veto) will be saved in ./SF_Output

'''


# parse the cutflow .txt file in the latex form and get the event numbers and uncertainties 
if len(sys.argv) != 3:
    print("Run this code by -> python <this code> <cutflow.txt in latex form> <bg, i.e. 'W+Jets' or 'DY+Jets'>")


# function that gets the scale factor and its error corresponding to the cut whose name is given as a parameter
def getScaleFactors(bg='W+Jets', cut='name of the cut'):
    # open the file
    f = open(sys.argv[1])

    parsed = []
    for line in f:
        if cut in line:
            parsed = line.split()

    numbers = []
    for item in parsed:
        try:
            item = float(item)
            numbers.append(item)
        except:
            #print("{} is not a number".format(item))
            item = False
    #print(parsed)
    #print(numbers)

    # for every item in the dictionary, <sample name>: [ <nEvent>, <stat. uncertainty> ]
    eventDic = {'Data':[numbers[0],0.], 'DPS_VV':[numbers[1],numbers[2]], 'DY+Jets':[numbers[3],numbers[4]], 'EWK_VV':[numbers[5],numbers[6]], 'EWK_W':[numbers[7],numbers[8]], 'EWK_Z':[numbers[9],numbers[10]], 'Higgs':[numbers[11],numbers[12]], 'QCD':[numbers[13],numbers[14]], 'SingleTop':[numbers[15],numbers[16]], 'V#gamma':[numbers[17],numbers[18]], 'VV':[numbers[19],numbers[20]], 'VVV': [numbers[21], numbers[22]], 'W+Jets': [numbers[23], numbers[24]], 't#bar{t}+X':[numbers[25],numbers[26]], 't#bar{t}':[numbers[27],numbers[28]]}
    #eventDic = {'Data':[numbers[0],0.], 'DPS_VV':[numbers[1],numbers[2]], 'DY+Jets':[numbers[3],numbers[4]], 'EWK_V':[numbers[5],numbers[6]], 'EWK_VV':[numbers[7],numbers[8]], 'Higgs':[numbers[9],numbers[10]], 'QCD':[numbers[11],numbers[12]], 'SingleTop':[numbers[13],numbers[14]], 'V#gamma':[numbers[15],numbers[16]], 'VV':[numbers[17],numbers[18]], 'VVV':[numbers[19],numbers[20]], 'W+Jets': [numbers[21], numbers[22]], 't#bar{t}+X': [numbers[23], numbers[24]], 't#bar{t}':[numbers[25],numbers[26]]}

    # propagate uncertainties
    nData = nProcess = nNonProcess = nTotalMC = 0.
    delta_nProcess = delta_nNonProcess = delta_nTotalMC = 0.
    delta_nNonProcess_squared = delta_nTotalMC_squared = 0.

    for key, value in eventDic.items():
       #print("{}: {} +/- {}".format(key, value[0], value[1]))
       if key == 'Data':
            nData += value[0]
            delta_nData = sqrt(nData)
       elif bg in key:
            nProcess += value[0]
            delta_nProcess += value[1]
            nTotalMC += value[0]
            delta_nTotalMC_squared += value[1]**2
       else:
            nNonProcess += value[0]
            delta_nNonProcess_squared += value[1]**2
            nTotalMC += value[0]
            delta_nTotalMC_squared += value[1]**2

    delta_nNonProcess = sqrt(delta_nNonProcess_squared)
    delta_nTotalMC = sqrt(delta_nTotalMC_squared)

    # calculate SF
    numerator = nData - nNonProcess
    delta_numerator = sqrt(delta_nData**2 + delta_nNonProcess**2)
    denominator = nProcess
    delta_denominator = delta_nProcess

    try:
        scaleFactor = numerator / denominator
        delta_scaleFactor = scaleFactor * sqrt( (delta_numerator/numerator)**2 + (delta_denominator/denominator)**2 )

    except:
        scaleFactor = delta_scaleFactor = 0. 

    # calculate purity
    purity_numerator = nProcess
    purity_denominator = nTotalMC
    delta_purity_numerator = delta_nProcess
    delta_purity_denominator = delta_nTotalMC

    purity = purity_numerator / purity_denominator
    delta_purity = purity * sqrt( (delta_purity_numerator/purity_numerator)**2 + (delta_purity_denominator/purity_denominator)**2 )

    # print out the results
    #print('\nSTEP = {}'.format(cut))
    #print('Data: {}'.format(nData))
    #print('{}: {} +/- {}'.format(bg, nProcess, delta_nProcess))
    #print('Non-{}: {} +/- {}'.format(bg, nNonProcess, delta_nNonProcess))
    #print('{} cut {}-SF: {:.3f} $\pm$ {:.3f}'.format(cut, bg, scaleFactor, delta_scaleFactor))
    return(scaleFactor, delta_scaleFactor, purity, delta_purity, nTotalMC, delta_nTotalMC, nData, delta_nData, nProcess, delta_nProcess)


# save the sf and its error as a txt file
def saveSF(year=2016, bg='W', cut='name of the cut'):
    outfile_name = 'SF.txt'
    outfile_dir = './SF_Output/'

    if 'CR1' in sys.argv[1]:
        outfile_name = '{}_SF_{}_Central.txt'.format(year, bg)
    elif 'CR2' in sys.argv[1]:
        outfile_name = '{}_SF_{}_Central+VBF.txt'.format(year, bg)

    if os.path.exists(outfile_dir+outfile_name):
        os.remove(outfile_dir+outfile_name)

    outfile = open(outfile_dir+outfile_name, 'a')
    outfile.write(str(getScaleFactors(bg, cut)[0])+' $\pm$ '+str(getScaleFactors(bg, cut)[1]))
    print("\nSaved: {}\n".format(outfile_dir+outfile_name))


# main func
if __name__ == '__main__':
    bg = sys.argv[2]   # i.e. W or DY
    
    if 'W+Jets' in bg:
        cutList = [ 'Trigger', 'Muon1', 'Muon2', 'MET', 'Jet1','Jet2', 'DiJet', 'Tau', 'BJet' ]
    elif 'DY+Jets' in bg:
        cutList = [ 'Trigger', 'Muon1', 'DiMuon', 'MET', 'Jet1','Jet2', 'DiJet', 'Tau', 'BJet' ]

    print('\n')

    if '2016' in sys.argv[1]:
        year = 2016
    elif '2017' in sys.argv[1]:
        year = 2017
    elif '2018' in sys.argv[1]:
        year = 2018

    for cut in cutList:
        if cut == 'DiJet' and 'CR1' in sys.argv[1]:
            continue
        #if cut == 'Muon2' and year != 2018:
        #    continue
        print('{} step {}-SF: {:.3f} $\pm$ {:.3f}, Purity: {:.3f} $\pm$ {:.3f}, Total MC: {:.1f} $\pm$ {:.1f}, Data: {:.1f} $\pm$ {:.1f}, Process: {:.1f} $\pm$ {:.1f}'.format(cut, bg, getScaleFactors(bg, cut)[0], getScaleFactors(bg,cut)[1], getScaleFactors(bg,cut)[2], getScaleFactors(bg,cut)[3], getScaleFactors(bg,cut)[4], getScaleFactors(bg,cut)[5], getScaleFactors(bg,cut)[6], getScaleFactors(bg,cut)[7], getScaleFactors(bg,cut)[8], getScaleFactors(bg,cut)[9]))
   
    #saveSF(year, bg, 'BJet')
