import sys
import os
from math import sqrt

'''
Usage:
1. Make sure you have cutflow output txt file from Plotter whose name specifies CR1 or CR2
2. Run the code by 
python3 scaleFactor.py <cutflow txt file> <bg: 'W' or 'DY'>
i.e, python3 scaleFactor.py Cutflow_from_Plotter/cutflow_2016_Z_CR1.txt DY
3. Scale factor for following steps will be printed
CR1) Trigger, Muon Selection, MET, Lepton Veto(after Tau veto), BJet Veto
CR2) Trigger, Muon Selection, MET, VBF Cuts, Lepton Veto(after Tau Veto), BJet Veto
4. Scale factor from the CR (after BJet Veto) will be saved in ./SF_Output

'''


# parse the cutflow .txt file in the latex form and get the event numbers and uncertainties 
if len(sys.argv) != 3:
    print("Run this code by -> python <this code> <cutflow.txt in latex form> <bg, i.e. 'W' or 'DY'>")


# function that gets the scale factor and its error corresponding to the cut whose name is given as a parameter
def getScaleFactors(bg='W', cut='name of the cut'):
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
    eventDic = {'Data':[numbers[0],0.], 'DYJets':[numbers[1],numbers[2]], 'Diboson':[numbers[3],numbers[4]], 'QCD': [numbers[5],numbers[6]], 'SingleTop': [numbers[7],numbers[8]], 'TTbar': [numbers[9],numbers[10]], 'WJets': [numbers[11],numbers[12]]}

    # propagate uncertainties
    nData = nProcess = nNonProcess = 0.
    delta_nData = sqrt(nData)
    delta_nProcess = delta_nNonProcess = 0.
    delta_nNonProcess_squared = 0.

    for key, value in eventDic.items():
       #print("{}: {} +/- {}".format(key, value[0], value[1]))
       if key == 'Data':
            nData += value[0]
       elif bg in key:
            nProcess += value[0]
            delta_nProcess += value[1]
       else:
            nNonProcess += value[0]
            delta_nNonProcess_squared += value[1]**2

    delta_nNonProcess = sqrt(delta_nNonProcess_squared)

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

    # print out the results
    #print('\nSTEP = {}'.format(cut))
    #print('Data: {}'.format(nData))
    #print('{}: {} +/- {}'.format(bg, nW, delta_nW))
    #print('Non-{}: {} +/- {}'.format(bg, nNonW, delta_nNonW))
    #print('{} cut {}-SF: {:.3f} $\pm$ {:.3f}'.format(cut, bg, scaleFactor, delta_scaleFactor))
    return(scaleFactor, delta_scaleFactor)


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
    
    if 'W' in bg:
        cutList = [ 'Trigger', 'Muon1', 'Muon2', 'MET', 'DiJet', 'Tau', 'BJet' ]
    elif 'DY' in bg:
        cutList = [ 'Trigger', 'Muon1', 'DiMuon', 'MET', 'DiJet', 'Tau', 'BJet' ]

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
        if cut == 'Muon2' and year != 2018:
            continue
        print('{} step {}-SF: {:.3f} $\pm$ {:.4f}'.format(cut, bg, getScaleFactors(bg, cut)[0], getScaleFactors(bg,cut)[1]))
   
    saveSF(year, bg, 'BJet')
