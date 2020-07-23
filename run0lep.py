#!/bin/env python

configDic = {'PartDet':'zjets', 'year': 2016}

import os,sys

datafile = sys.argv[1]
configDic['datafile'] = datafile
configDic['outname'] = datafile.split('/')[5] + '.root'

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
if not os.path.isdir(configDic['PartDet']):
    os.system('ln -s $CMSSW_BASE/src/vbfsusy/{PartDet} .'.format(**configDic))
    
runcode = '$CMSSW_BASE/src/NanoAOD_Analyzer/Analyzer -out {outname} -y {year} -C {PartDet} -in {datafile} '.format(**configDic)
print(runcode)
os.system(runcode)

# run0lep.py /hdfs/store/data/Run2016C/SingleMuon/NANOAOD/Nano1June2019-v1/30000/F67E58A1-F245-984D-8953-BEB8ECD16B84.root
# run0lep.py /hdfs/store/mc/RunIISummer16NanoAODv6-largeblock/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/NANOAODSIM/PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v2/20000/7378B9CD-404E-B045-9E05-E261D30BC883.root
# run0lep.py /hdfs/store/mc/RunIISummer16NanoAODv6-largeblock/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/NANOAODSIM/PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/270000/0F95EA56-FF3C-A940-A3F7-0BABD701D91D.root
