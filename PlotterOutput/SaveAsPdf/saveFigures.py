'''

Get a plotter output root file and a config file that contains the options for saving the figures from the plotter output 
And save them following the options

Usage: python saveFigures.py --config <saveOptions.config> --input_file <input root file>

Kyungmin Park (kyungmin.park@cern.ch; jazzykm0110@uos.ac.kr)

'''

import os, sys, getopt

# get option config file and input root file as arguments
try:
    opts, args = getopt.getopt(sys.argv[1:], "c:f:", ["config=", "input_file="])
except getopt.GetoptError:
    print("\nUsage: python saveFigures.py --config <saveOptions.config> --input_file <input root file>\n") 
    sys.exit()

has_config = False
has_input_file = False
for opt, arg in opts:
    if opt in ("-c", "--config"):
        config = arg
        has_config = True
    elif opt in ("-f", "--input_file"):
        input_file = arg
        has_input_file = True

if has_config == False or has_input_file == False:
    if has_config == False:
        print("\nConfig file is not given.")
    if has_input_file == False:
        print("\nInput root file is not given.")
    print("\nUsage: python saveFigures.py --config <saveOptions.config> --input_file <input root file>\n")
    sys.exit()

# Read from option config file and run ./src/redrawSave.py that saves the figure with the given options
f = open(config)
parsed = []
for line in f:
    if len(line.strip()) == 0 or "#" in line:
        continue
    
    print("\n")
    parsed = line.split()

    run_code = "python ./src/redrawSave.py --input_file {}".format(input_file)
    
    for i in range(len(parsed)):
        if "--" in parsed[i]:
            run_code += " {} {}".format(parsed[i], parsed[i+1])
        else:
            continue 
    print(run_code)
    os.system(run_code)
