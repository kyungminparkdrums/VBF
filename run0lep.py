#!/bin/env python
import os,sys

'''
Usage

1. Data
run0lep.py /hdfs/store/data/Run2016C/SingleMuon/NANOAOD/Nano1June2019-v1/30000/F67E58A1-F245-984D-8953-BEB8ECD16B84.root
2. MC
run0lep.py /hdfs/store/mc/RunIISummer16NanoAODv6-largeblock/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/NANOAODSIM/PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v2/20000/7378B9CD-404E-B045-9E05-E261D30BC883.root
3. MC (Inclusive DY and WJets that need HTFilter on)
run0lep.py /hdfs/store/mc/RunIISummer16NanoAODv6-largeblock/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/NANOAODSIM/PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/270000/0F95EA56-FF3C-A940-A3F7-0BABD701D91D.root

'''

partDetDir = '$CMSSW_BASE/src/vbfsusy/PartDets/2017/W_CR2/'
configDic = {'PartDet':partDetDir+'wjets', 'year': 2017}

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

if 'DYJetsToLL_M-50_T' in datafile or 'WJetsToLNu_T' in datafile:
    configDic['PartDet'] +='_htfilter'
    
if not os.path.isdir('Pileup'):
    os.system('ln -s $CMSSW_BASE/src/NanoAOD_Analyzer/Pileup .')    
#if not os.path.isdir(configDic['PartDet']):
#    os.system('ln -s $CMSSW_BASE/src/vbfsusy/{PartDet} .'.format(**configDic))

# Rename the output files for 2017 samples (for the SpecialPUCalculation); the output file name should be one of the branch names from PileUp/new_mc2017_pileupReweighting_NanoAODv6.root
if configDic['year'] == 2017 and not 'data' in datafile:
    if '_TuneCP5' in datafile:
        configDic['outname'] = (datafile.split('/')[5]).split('_TuneCP5')[0] + '_TuneCP5.root'
    elif '_13TeV' in datafile:
        configDic['outname'] = (datafile.split('/')[5]).split('_13TeV')[0] + '_13TeV.root'
    
runcode = '$CMSSW_BASE/src/NanoAOD_Analyzer/Analyzer -out {outname} -y {year} -C {PartDet} -in {datafile} '.format(**configDic)
print(runcode)
os.system(runcode)

