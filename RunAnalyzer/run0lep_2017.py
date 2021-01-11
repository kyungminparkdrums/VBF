#!/bin/env python
import os,sys

'''
Usage

1. Data
python3 run0lep_2017.py /hdfs/store/data/Run2017E/SingleMuon/NANOAOD/Nano25Oct2019-v1/40000/F336498B-2475-3648-B846-B0BF398C66B3.root

2. MC
python3 run0lep_2017.py /hdfs/store/mc/RunIIFall17NanoAODv6/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_new_pmx_102X_mc2017_realistic_v7-v1/100000/02227F9D-F735-FA40-9D9F-C39D70BA629A.root

3. MC (Inclusive DY and WJets that need HTFilter on)
python3 run0lep_2017.py /hdfs/store/mc/RunIIFall17NanoAODv6/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017RECOSIMstep_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/280000/F6C26D24-0C0A-8144-BDE2-54446845263C.root

'''

partDetDir = '$CMSSW_BASE/src/vbfsusy/PartDets/2017/Z_CR2/'
configDic = {'PartDet':partDetDir+'zjets', 'year': 2017}

#partDetDir = '$CMSSW_BASE/src/vbfsusy/PartDets/2017/W_CR2/'
#configDic = {'PartDet':partDetDir+'wjets', 'year': 2017}

datafile = sys.argv[1]
configDic['datafile'] = datafile
configDic['outname'] = datafile.split('/')[4] + '.root'

# Get PartDets
if 'data' in datafile:
    if 'B_ver1' in datafile or 'B_ver2' in datafile:  # i.e. SingleMuon_Run2016B.root, not SingleMuon_Run2016B_ver1.root
        configDic['outname'] = 'SingleMuon_Run2016B.root'
    else:
        configDic['outname'] = datafile.split('/')[4] + '_' + datafile.split('/')[3] + '.root'
    configDic['PartDet'] +='_data'

if 'DYJetsToLL_M-10to50_T' in datafile or 'DYJetsToLL_M-50_T' in datafile:
    configDic['PartDet'] +='_htfilter'
    
if 'WJetsToLNu_T' in datafile and not 'TTWJets' in datafile:
    configDic['PartDet'] +='_htfilter'

if not os.path.isdir('Pileup'):
    os.system('ln -s $CMSSW_BASE/src/NanoAOD_Analyzer/Pileup .')    

# Rename the output files for 2017 samples (for the SpecialPUCalculation); the output file name should be one of the branch names from PileUp/new_mc2017_pileupReweighting_NanoAODv6.root
if configDic['year'] == 2017 and not 'data' in datafile:
    if '_TuneCP5' in datafile:
        configDic['outname'] = (datafile.split('/')[4]).split('_TuneCP5')[0] + '_TuneCP5.root'
    elif '_13TeV' in datafile:
        configDic['outname'] = (datafile.split('/')[4]).split('_13TeV')[0] + '_13TeV.root'
    
runcode = '$CMSSW_BASE/src/NanoAOD_Analyzer/Analyzer -out {outname} -y {year} -C {PartDet} -in {datafile} '.format(**configDic)
#runcode = '$CMSSW_BASE/src/Forked/NanoAOD_Analyzer/Analyzer -out {outname} -y {year} -C {PartDet} -in {datafile} '.format(**configDic)

if len(sys.argv) == 3 and '-t' in sys.argv[2]:
    runcode += ' -t'

print(runcode)
os.system(runcode)

