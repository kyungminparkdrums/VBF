#!/bin/env python
import os,sys

'''
Usage

1. Change options in line 17-18 if necessary
2. Change options in line 193 if necessary
2. Change line 22

Then, simply run
python3 batch_2017.py

'''

executableCode = '$CMSSW_BASE/src/vbfsusy/RunAnalyzer/run0lep_2017.py'
runData = False
runMC = True

# set output directory
hostDir = '/home/scratch/'
outDir = hostDir + os.environ.get('USER') + '/2017/test/'

if not os.path.exists(outDir):
    os.makedirs(outDir)
    print('\nOutput directory {} does not exist. \nCreating it .. \n'.format(outDir))

# Data
dataDir = '/store/data/Run2017'
dataList = [ 'B', 'C', 'D', 'E', 'F' ]

# MC
mcDir = '/store/mc/RunIIFall17NanoAODv6/'

TTbar = [
    'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8',
    'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8',
    'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8',
]

SingleTop = [
    'ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8',
    'ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
    'ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
    'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8',
    'ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8',
]

ZJets = [
    # Inclusive
    'DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8',
    'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
    
    # DY+Jets M-4to50
    'DYJetsToLL_M-4to50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8',
    'DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8',
    'DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8',
    'DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8',
    
    # DY+Jets M-50
    'DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8',
    'DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8',
    'DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8',
    'DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8',
    'DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8',
    'DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8',
    'DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8',
]

DiBoson = [
    # WW
    'WWTo2L2Nu_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8',
    'WWTo4Q_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8',
    'WWToLNuQQ_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8',
    'WWJJToLNuLNu_EWK_QCD_noTop-noHiggs_TuneCP5_13TeV-madgraph-pythia8',
    'WpWpJJ_QCD_TuneCP5_13TeV-madgraph-pythia8',
    'GluGluToWWToENEN_13TeV_MCFM701_pythia8',
    'GluGluToWWToENMN_13TeV_MCFM701_pythia8',
    'GluGluToWWToENTN_13TeV_MCFM701_pythia8',
    'GluGluToWWToMNEN_13TeV_MCFM701_pythia8',
    'GluGluToWWToMNMN_13TeV_MCFM701_pythia8',
    'GluGluToWWToMNTN_13TeV_MCFM701_pythia8',
    'GluGluToWWToTNEN_13TeV_MCFM701_pythia8',
    'GluGluToWWToTNMN_13TeV_MCFM701_pythia8',
    'GluGluToWWToTNTN_13TeV_MCFM701_pythia8',

    # WZ
    'WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8',
    'WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2',
    'WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8',
    'WZTo3LNu_13TeV-powheg-pythia8',

    # ZZ
    'ZZTo2L2Nu_13TeV_powheg_pythia8',
    'ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8',
    'ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8',
    'ZZTo4L_13TeV_powheg_pythia8',
]

WJets = [
    # Inclusive
    'WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8',
    
    # HT-binned
    'WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8',
]

QCD = [
    'QCD_HT50to100_TuneCP5_13TeV-madgraphMLM-pythia8',
    'QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8',
    'QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8',
    'QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8',
    'QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8',
    'QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8',
    'QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8',
    'QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8',
    'QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8',
]

VBS_VBF_DiBoson = [
    'WpWpJJ_EWK_TuneCP5_13TeV-madgraph-pythia8',
    'WWJJToLNuLNu_EWK_noTop_TuneCP5_13TeV-madgraph-pythia8',
    'WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8',
    'ZZJJTo4L_EWK_TuneCP5_13TeV-madgraph-pythia8',
]

WW_ZZ_DoublePartonScattering = [
    'WWTo2L2Nu_DoubleScattering_13TeV-pythia8',
    'ZZTo4L_TuneCP5_DoubleScattering_13TeV-pythia8',
]

V_gamma = [
    'WGJJToLNu_EWK_QCD_TuneCP5_13TeV-madgraph-pythia8',
    'LLAJJ_EWK_MLL-50_MJJ-120_TuneCP5_13TeV-madgraph-pythia8',
    'ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8',
    'LNuAJJ_EWK_MJJ-120_TuneCP5_13TeV-madgraph-pythia8',
]

VBS_VBF_WorZJets = [
    'EWKWMinus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8',
    'EWKWPlus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8',
    'EWKZ2Jets_ZToLL_M-50_TuneCP5_13TeV-madgraph-pythia8',
    'EWKZ2Jets_ZToNuNu_TuneCP5_13TeV-madgraph-pythia8',
]

Higgs = [
    'VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8',
    'VBFHToBB_M-125_13TeV_powheg_pythia8_weightfix',
    'GluGluHToBB_M125_TuneCP5_13TeV-powheg-pythia8',
    'GluGluHToZZTo2L2Q_M125_13TeV_powheg2_JHUGenV7011_pythia8',
    'GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8',
    'ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8',
    'ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8',
    'ttH_HToZZ_4LFilter_M125_13TeV_powheg2_JHUGenV7011_pythia8',
]

TT_X = [
    'TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8',
    'TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8',
    'TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8',
    'TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8',
    'TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8',
    'TTTT_TuneCP5_13TeV-amcatnlo-pythia8',
]

TriBoson = [
    'WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8',
    'WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8',
    'WZZ_TuneCP5_13TeV-amcatnlo-pythia8',
    'ZZZ_TuneCP5_13TeV-amcatnlo-pythia8',
]

# Run over data
for i in dataList:
    dataName = 'SingleMuon_Run2017{}'.format(i)
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
        # Rename the output files for 2017 samples (for the SpecialPUCalculation); the output file name should be one of the branch names from PileUp/new_mc2017_pileupReweighting_NanoAODv6.root
        if '_TuneCP5' in i:
            mcJobDic['outputFile'] = i.split('_TuneCP5')[0] + '_TuneCP5.root'
        elif '_13TeV' in i:
            mcJobDic['outputFile'] = i.split('_13TeV')[0] + '_13TeV.root'
        runCode = '~/cpluostools/hadoopCondorSubmit.py {jobName} -e {executedCode} -o {outputFile} -d {inputFile} --outputdir {outputDir}'.format(**mcJobDic)

        if runMC == True:
            os.system('mkdir -p {}'.format(outDir+i))
            print(runCode)
            os.system(runCode)
