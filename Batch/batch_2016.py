#!/bin/env python
import os,sys

'''
Usage

1. Change options in line 17-18 if necessary
2. Change options in line 213 if necessary 
2. Change line 22

Then, simply run
python3 batch_2016.py

'''

executableCode = '$CMSSW_BASE/src/vbfsusy/RunAnalyzer/run0lep_2016.py'
runData = False
runMC = True

# set output directory
hostDir = '/home/scratch/'
outDir = hostDir + os.environ.get('USER') + '/2016/test/'

if not os.path.exists(outDir):
    os.makedirs(outDir)
    print('\nOutput directory {} does not exist. \nCreating it .. \n'.format(outDir))

# Data
dataDir = '/data/Run2016'
dataList = [ 'B_ver1', 'B_ver2', 'C', 'D', 'E', 'F', 'G', 'H' ]

# MC
mcDir = '/mc/RunIISummer16NanoAODv6/'

TTbar = [
    'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8',
    'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8',
    'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8',    
]

SingleTop = [
    'ST_s-channel_4f_leptonDecays_13TeV_PSweights-amcatnlo-pythia8',
    'ST_t-channel_antitop_4f_inclusiveDecays_13TeV_PSweights-powhegV2-madspin',
    'ST_t-channel_top_4f_inclusiveDecays_13TeV_PSweights-powhegV2-madspin',
    'ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1',
    'ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1',    
]

ZJets = [
    # Inclusive DY+Jets
    'DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 

    # DY+Jets M-5to50
    'DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 
    'DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',

    # DY+Jets M-50
    'DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',   
    'DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
]

DiBoson = [
    # WW
    'WWTo2L2Nu_13TeV-powheg',
    'WWTo4Q_13TeV-powheg',
    'WWToLNuQQ_13TeV-powheg',
    'WpWpJJ_QCD_TuneCUETP8M1_13TeV-madgraph-pythia8',
    'WWJJToLNuLNu_EWK_QCD_noTop-noHiggs_13TeV-madgraph-pythia8',
    'GluGluWWTo2L2Nu_MCFM_13TeV',

    # WZ
    'WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8',
    'WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8',
    'WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8',
    'WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8',

    # ZZ
    'ZZTo2L2Nu_13TeV_powheg_pythia8_ext1',
    'ZZTo2L2Q_13TeV_powheg_pythia8',
    'ZZTo2Q2Nu_13TeV_powheg_pythia8',
    'ZZTo4L_13TeV_powheg_pythia8',
    'ZZTo4Q_13TeV_amcatnloFXFX_madspin_pythia8', 
]

WJets = [
    'WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 
    'WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 
    'WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',   
]

QCD = [
    'QCD_HT50to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
]

VBS_VBF_DiBoson = [ 
    'WWJJToLNuLNu_EWK_noTop_13TeV-madgraph-pythia8',
    'WpWpJJ_EWK_TuneCUETP8M1_13TeV-madgraph-pythia8',
    'ZZJJTo4L_EWK_13TeV-madgraph-pythia8',
    'ZZJJ_ZZTo2L2Nu_EWK_13TeV-madgraph-pythia8',
    'WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8',
]

WW_ZZ_DoublePartonScattering = [
    'WWTo2L2Nu_DoubleScattering_13TeV-pythia8',
    'ZZTo4L_DoubleScattering_13TeV-pythia8',  # 'ZZTo4L_TuneCP5_DoubleScattering'
]

VBS_VBF_WorZJets = [
    'EWKWMinus2Jets_WToLNu_M-50_13TeV-madgraph-pythia8',
    'EWKWPlus2Jets_WToLNu_M-50_13TeV-madgraph-pythia8',
    'EWKZ2Jets_ZToLL_M-50_13TeV-madgraph-pythia8',
    'EWKZ2Jets_ZToNuNu_13TeV-madgraph-pythia8',  
]

Higgs = [
    'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8',
    'VBF_HToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8',
    'WPlusH_HToMuMu_M125_13TeV_powheg_pythia8',
    'WMinusH_HToMuMu_M125_13TeV_powheg_pythia8',
    'ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUgenV6_pythia8',    
    'ttH_HToZZ_4LFilter_M125_13TeV_powheg2_JHUgenV6_pythia8',
    'VBFHToBB_M-125_13TeV_powheg_pythia8',
    'GluGluHToBB_M125_13TeV_powheg_pythia8',
    'WplusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8',
    'WminusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8',
    'ZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8',
    'ggZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8',
    'bbHToBB_M-125_4FS_yb2_13TeV_amcatnlo',
]

TT_X = [
    'TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8',
    'TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8',
    'TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
    'TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
    'TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8',
    'TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
]

TriBoson = [
    'WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
    'WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
    'WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
    'ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
]

V_gamma = [
    'WGJJToLNu_EWK_QCD_TuneCUETP8M1_13TeV-madgraph-pythia8',
    'LLAJJ_EWK_MLL-50_MJJ-120_13TeV-madgraph-pythia8',
    'LNuAJJ_EWK_MJJ-120_TuneCUETP8M1_13TeV-madgraph-pythia8',
    'ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
]

unusedSamples = [ 
           # HT binned Z NuNu (for signal region)
#           'ZJetsToNuNu_HT-100To200_13TeV-madgraph',
#           'ZJetsToNuNu_HT-200To400_13TeV-madgraph',
#           'ZJetsToNuNu_HT-400To600_13TeV-madgraph',
#           'ZJetsToNuNu_HT-600To800_13TeV-madgraph',
#           'ZJetsToNuNu_HT-800To1200_13TeV-madgraph',
#           'ZJetsToNuNu_HT-1200To2500_13TeV-madgraph',
#           'ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph',

#           'TT_TuneCUETP8M2T4_13TeV-powheg-pythia8',
#           'WW_TuneCUETP8M1_13TeV-pythia8', 
#           'WZ_TuneCUETP8M1_13TeV-pythia8', 
#           'ZZ_TuneCUETP8M1_13TeV-pythia8' 
]


# Run over data
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

    dataJobDic = {'executedCode':executableCode, 'jobName':dataName, 'outputFile':dataName+'.root', 'inputFile':dataDir+i+'/SingleMuon/NANOAOD/'+dataVersion, 'outputDir':outDir+dataName}
    runCode = '~/cpluostools/hadoopCondorSubmit.py {jobName} -e {executedCode} -o {outputFile} -d {inputFile} --outputdir {outputDir}'.format(**dataJobDic)
    
    if runData == True:
        os.system('mkdir -p {}'.format(outDir+dataName))
        print(runCode)
        os.system(runCode)

# Run over MC
mcList = [ TTbar, SingleTop, ZJets, DiBoson, WJets, QCD, VBS_VBF_DiBoson, WW_ZZ_DoublePartonScattering, VBS_VBF_WorZJets, VBS_VBF_WorZJets, Higgs, TT_X, TriBoson, V_gamma ]

for samples in mcList:
    for i in samples:
        mcJobDic = {'executedCode':executableCode, 'jobName':i, 'outputFile':i+'.root', 'inputFile':mcDir+i, 'outputDir':outDir+i}
        runCode = '~/cpluostools/hadoopCondorSubmit.py {jobName} -e {executedCode} -o {outputFile} -d {inputFile} --outputdir {outputDir}'.format(**mcJobDic)

        if runMC == True:
            os.system('mkdir -p {}'.format(outDir+i))
            print(runCode)
            os.system(runCode)
