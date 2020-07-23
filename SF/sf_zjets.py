import sys
import os
from math import sqrt

# parse the cutflow .txt file in the latex form and get the event numbers and uncertainties 
if len(sys.argv) != 2:
    print("Run this code by -> python <this code> <cutflow.txt in latex form>")

f = open(sys.argv[1])
for line in f:
    if 'BJet' in line:
        parsed = line.split()

numbers = []
for item in parsed:
    try:
        item = float(item)
        numbers.append(item)
    except:
        item = False
        #print("{} is not a number".format(item))
#print(parsed)
#print(numbers)


# for every item in the dictionary, <sample name>: [ <nEvent>, <stat. uncertainty> ]
eventDic = {'Data':[numbers[0],0.], 'DYJets':[numbers[1],numbers[2]], 'Diboson':[numbers[3],numbers[4]], 'QCD': [numbers[5],numbers[6]], 'SingleTop': [numbers[7],numbers[8]], 'TTbar': [numbers[9],numbers[10]], 'WJets': [numbers[11],numbers[12]]}


# propagate uncertainties
nData = nDY = nNonDY = 0.
delta_nDY = delta_nNonDY = 0.
delta_nNonDY_squared = 0.

for key, value in eventDic.items():
    print("{}: {} +/- {}".format(key, value[0], value[1]))
    if key == 'Data':
        nData += value[0]
    elif key == 'DYJets':
        nDY += value[0]
        delta_nDY += value[1]
    else:
        nNonDY += value[0]
        delta_nNonDY_squared += value[1]**2

delta_nNonDY = sqrt(delta_nNonDY_squared)


# calculate SF
numerator = nData - nNonDY
delta_numerator = delta_nNonDY
denominator = nDY
delta_denominator = delta_nDY

try:
    scaleFactor = numerator / denominator
    delta_scaleFactor = scaleFactor * sqrt( (delta_numerator/numerator)**2 + (delta_denominator/denominator)**2 )

except:
    scaleFactor = delta_scaleFactor = 0. 
    

# print out the results
print('\nData: {}'.format(nData))
print('DY: {} +/- {}'.format(nDY, delta_nDY))
print('Non-DY: {} +/- {}'.format(nNonDY, delta_nNonDY))
print('\nSF: {} +/- {}'.format(scaleFactor, delta_scaleFactor))


# save the sf in a new txt file
outfile_name = 'sf_z.txt'
if 'cr1' in sys.argv[1]:
    outfile_name = 'sf_z_cr1.txt'
elif 'cr2' in sys.argv[1]:
    outfile_name = 'sf_z_cr2.txt'

if os.path.exists(outfile_name):
    os.remove(outfile_name)

outfile = open(outfile_name, 'a')
outfile.write(str(scaleFactor)+" +/- "+str(delta_scaleFactor))
print("\nSaved: {}".format(outfile_name))
