#!/bin/env python
import os,sys

'''
Usage

1. Data
python3 run0lep_2016.py /hdfs/store/data/Run2016C/SingleMuon/NANOAOD/Nano1June2019-v1/30000/F67E58A1-F245-984D-8953-BEB8ECD16B84.root

2. MC
python3 run0lep_2016.py /hdfs/store/mc/RunIISummer16NanoAODv6/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/NANOAODSIM/PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/60000/050890BC-AD67-B343-85BD-8B0956135E6B.root

3. MC (Inclusive DY and WJets that need HTFilter on)
python3 run0lep_2016.py /hdfs/store/mc/RunIISummer16NanoAODv6-largeblock/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/NANOAODSIM/PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/270000/0F95EA56-FF3C-A940-A3F7-0BABD701D91D.root

'''

partDetDir = '$CMSSW_BASE/src/vbfsusy/PartDets/2016/Z_CR2/'
configDic = {'PartDet':partDetDir+'zjets', 'year': 2016}

#partDetDir = '$CMSSW_BASE/src/vbfsusy/PartDets/2016/W_CR2/'
#configDic = {'PartDet':partDetDir+'wjets', 'year': 2016}

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

