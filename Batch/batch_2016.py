#!/bin/env python
import os,sys

'''

Submit batch jobs for BSM3G NanoAOD analyzer with hadoopSubmitCondor.py
Written by Kyungmin Park (jazzykm0110@uos.ac.kr)

'''

executableCode = '../run0lep.py'
outDir = '/home/scratch/kmpark/test/'

dataDir = '/store/data/Run2016'
dataList = [ 'B_ver1', 'B_ver2', 'C', 'D', 'E', 'F', 'G', 'H' ]

mcDir = '/store/mc/RunIISummer16NanoAODv6/'
mcList = [ 
           # HT binned DY jets 
           'DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'EWKZ2Jets_ZToLL_M-50_13TeV-madgraph-pythia8', 
           # HT binned W jets
           'WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'EWKWPlus2Jets_WToLNu_M-50_13TeV-madgraph-pythia8', 'EWKWMinus2Jets_WToLNu_M-50_13TeV-madgraph-pythia8', 
           # QCD
           'QCD_HT50to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',             
           # TTbar
           'TT_TuneCUETP8M2T4_13TeV-powheg-pythia8', 
           # Single Top
           'ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1', 'ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1', 'ST_t-channel_top_4f_inclusiveDecays_13TeV_PSweights-powhegV2-madspin', 'ST_t-channel_antitop_4f_inclusiveDecays_13TeV_PSweights-powhegV2-madspin', 
           # Diboson
           'WW_TuneCUETP8M1_13TeV-pythia8', 'WZ_TuneCUETP8M1_13TeV-pythia8', 'ZZ_TuneCUETP8M1_13TeV-pythia8', 
           # inclusive DY and WJets
           'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8' 
]

for i in mcList:
    os.system('mkdir -p {}'.format(outDir+i))
    mcJobDic = {'executedCode':executableCode, 'jobName':i, 'outputFile':i+'.root', 'inputFile':mcDir+i, 'outputDir':outDir+i}
    runCode = '~/cpluostools/hadoopCondorSubmit.py {jobName} -e {executedCode} -o {outputFile} -d {inputFile} --outputdir {outputDir}'.format(**mcJobDic)
    print(runCode)
    os.system(runCode)


for i in dataList:
    if i == 'B_ver1':
        dataName = 'SingleMuon_Run2016B'
        dataVersion = 'Nano25Oct2019_ver1-v1'
    elif i == 'B_ver2':
        dataName = 'SingleMuon_Run2016B'
        dataVersion = 'Nano25Oct2019_ver2-v1'
    else:
        dataName = 'SingleMuon_Run2016{}'.format(i)
        dataVersion = 'Nano25Oct2019-v1'    

    os.system('mkdir -p {}'.format(outDir+dataName))
    dataJobDic = {'executedCode':executableCode, 'jobName':dataName, 'outputFile':dataName+'.root', 'inputFile':dataDir+i+'/SingleMuon/NANOAOD/'+dataVersion, 'outputDir':outDir+dataName}
    runCode = '~/cpluostools/hadoopCondorSubmit.py {jobName} -e {executedCode} -o {outputFile} -d {inputFile} --outputdir {outputDir}'.format(**dataJobDic)
    print(runCode)
    os.system(runCode)


