#!/bin/env python
import os,sys

'''
Usage

1. Data
python3 run0lep_2018.py /hdfs/store/data/Run2018B/SingleMuon/NANOAOD/Nano25Oct2019-v1/30000/BBA7048A-66A4-BB4E-ABE8-B8562B47BB6E.root

2. MC
python3 run0lep_2018.py /hdfs/store/mc/RunIIAutumn18NanoAODv6/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/NANOAODSIM/Nano25Oct2019_102X_upgrade2018_realistic_v20_ext2-v1/250000/AC9AC9C6-9375-A744-A60B-88E6C36C9D17.root

3. MC (Inclusive DY and WJets that need HTFilter on)
python3 run0lep_2018.py /hdfs/store/mc/RunIIAutumn18NanoAODv6/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/40000/AD6EBF30-5BFA-0D43-A28B-47F473ECECA6.root

'''

partDetDir = '$CMSSW_BASE/src/vbfsusy/PartDets/2018/Z_CR1/'
configDic = {'PartDet':partDetDir+'zjets', 'year': 2018}

#partDetDir = '$CMSSW_BASE/src/vbfsusy/PartDets/2018/W_CR1/'
#configDic = {'PartDet':partDetDir+'wjets', 'year': 2018}

datafile = sys.argv[1]
configDic['datafile'] = datafile
configDic['outname'] = datafile.split('/')[5] + '.root'

# Get PartDets
if 'data' in datafile:
    if 'B_ver1' in datafile or 'B_ver2' in datafile:  # i.e. SingleMuon_Run2016B.root, not SingleMuon_Run2016B_ver1.root
        configDic['outname'] = 'SingleMuon_Run2016B.root'
    else:
        configDic['outname'] = datafile.split('/')[5] + '_' + datafile.split('/')[4] + '.root'
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
        configDic['outname'] = (datafile.split('/')[5]).split('_TuneCP5')[0] + '_TuneCP5.root'
    elif '_13TeV' in datafile:
        configDic['outname'] = (datafile.split('/')[5]).split('_13TeV')[0] + '_13TeV.root'
    
runcode = '$CMSSW_BASE/src/NanoAOD_Analyzer/Analyzer -out {outname} -y {year} -C {PartDet} -in {datafile} '.format(**configDic)
#runcode = '$CMSSW_BASE/src/Forked/NanoAOD_Analyzer/Analyzer -out {outname} -y {year} -C {PartDet} -in {datafile} '.format(**configDic)

if len(sys.argv) == 3 and '-t' in sys.argv[2]:
    runcode += ' -t'

print(runcode)
os.system(runcode)

