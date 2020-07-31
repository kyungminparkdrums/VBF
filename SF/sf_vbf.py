import sys
import os
from math import sqrt

# parse the cutflow .txt file in the latex form and get the SFs and uncertainties 
if len(sys.argv) != 3:
    print("Run this code by -> python <this code> <sf_cr1.txt> <sf_cr2.txt>")

sf = [ 0., 0. ]
delta_sf = [ 0., 0. ]

for i in range(2):
    f = open(sys.argv[i+1])
    for line in f:
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
    sf[i] = numbers[0]
    delta_sf[i] = numbers[1]

#print(sf)
#print(delta_sf)


# calculated VBF SF
numerator = sf[1]     # SF_CR2
delta_numerator = delta_sf[1]  
denominator = sf[0]   # SF_CR1
delta_denominator = delta_sf[0]

scaleFactor = numerator / denominator
delta_scaleFactor = scaleFactor * sqrt((delta_denominator/denominator)**2 + (delta_numerator/numerator)**2) 

print('\nVBF SF: {:.3f} $\pm$ {:.3f}'.format(scaleFactor, delta_scaleFactor))
