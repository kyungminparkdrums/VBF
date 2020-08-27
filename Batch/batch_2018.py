#!/bin/env python
import os,sys

'''

Submit batch jobs for BSM3G NanoAOD analyzer with hadoopSubmitCondor.py
Kyungmin Park (jazzykm0110@uos.ac.kr)

'''

executableCode = '$CMSSW_BASE/src/vbfsusy/run0lep.py'
hostDir = '/home/scratch/'
outDir = hostDir + os.environ.get('USER') + '/2018/Z_CR1/'

if not os.path.exists(outDir):
    os.makedirs(outDir)
    print('\nOutput directory {} does not exist. \nCreating it .. \n'.format(outDir))

dataDir = '/store/data/Run2018'
dataList = [ 'A', 'B', 'C', 'D' ]

mcDir = '/store/mc/RunIIAutumn18NanoAODv6/'
mcList = [ 
           # Low Mass HT-binned DY jets
           'DYJetsToLL_M-4to50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', 
           'DYJetsToLL_M-4to50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
           'DYJetsToLL_M-4to50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
           'DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8',

           # HT binned DY jets 
           'DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
           'DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
           'DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
           'DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
           'DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
           'DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
           'DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
           'EWKZ2Jets_ZToLL_M-50_TuneCP5_PSweights_13TeV-madgraph-pythia8',

           # HT binned W jets
           'WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8',
           'WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8',
           'WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8',
           'WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8',
           'WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8',
           'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8',
           'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8',
           'EWKWMinus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8',
           'EWKWPlus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8',           

           # inclusive DY and WJets
           'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
           'WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8',

           # QCD
           'QCD_HT100to200_TuneCP5_13TeV-madgraphMLM-pythia8',
           'QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8',
           'QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8',
           'QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8',
           'QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8',
           'QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8',
           'QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8',
           'QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8',
           
           # TTbar
           'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8',
           'TTToHadronic_TuneCP5_13TeV-powheg-pythia8',
           'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8',           

           # Single Top
           'ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8',
           'ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8',
           'ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8',
           'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8',

           # Diboson
           'WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8',
           'WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8',
           'WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8', 
           'WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8',
           'WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8',
           'WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8',
           'WZTo3LNu_TuneCP5_13TeV-powheg-pythia8',
           'ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8',
           'ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8',
           'ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8',
           'ZZTo4L_13TeV_powheg_pythia8_TuneCP5'
]


# Run over data
for i in dataList:
    dataName = 'SingleMuon_Run2018{}'.format(i)
    dataVersion = 'Nano25Oct2019-v1'    

    os.system('mkdir -p {}'.format(outDir+dataName))
    dataJobDic = {'executedCode':executableCode, 'jobName':dataName, 'outputFile':dataName+'.root', 'inputFile':dataDir+i+'/SingleMuon/NANOAOD/'+dataVersion, 'outputDir':outDir+dataName}
    runCode = '~/cpluostools/hadoopCondorSubmit.py {jobName} -e {executedCode} -o {outputFile} -d {inputFile} --outputdir {outputDir}'.format(**dataJobDic)
    print(runCode)
    os.system(runCode)


# Run over MC
for i in mcList:
    os.system('mkdir -p {}'.format(outDir+i))
    mcJobDic = {'executedCode':executableCode, 'jobName':i, 'outputFile':i+'.root', 'inputFile':mcDir+i, 'outputDir':outDir+i}
    runCode = '~/cpluostools/hadoopCondorSubmit.py {jobName} -e {executedCode} -o {outputFile} -d {inputFile} --outputdir {outputDir}'.format(**mcJobDic)
    print(runCode)
    os.system(runCode)
