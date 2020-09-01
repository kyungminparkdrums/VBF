#!/bin/bash

# hadd data output files: i.e, hadd from SingleMuon_Run2016B.root to SingleMuon_Run2016H.root --> SingleMuon_Run2016.root as output
# 1. After you ran over all files
# 2. Run merge code
# 3. There will be newly created 'results_merged' folder in the output directory where the merged output root files are stored
# 4. Outside the 'results_merged' folder, run ./hadd.sh
# 5. i.e, SingleMuon_Run2016.root will be saved in pwd

# for 2016 samples
hadd -f ./SingleMuon_Run2016.root ./results_merged/SingleMuon_Run2016[B-H].root

# for 2017 samples
#hadd -f ./SingleMuon_Run2017.root ./results_merged/SingleMuon_Run2017[B-F].root

# for 2018 samples
#hadd -f ./SingleMuon_Run2018.root ./results_merged/SingleMuon_Run2018[A-D].root
