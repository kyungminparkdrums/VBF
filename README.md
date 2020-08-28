# VBF
VBF 0 lepton

# Batch
Batch submitting code (2016 - 2018) with `run0lep.py` and `hadoopCondorSubmit.py` for UOS gate users

# PartDets
Config files for wjets and zjets background estimation, respectively
- **CR1)** CENTRAL: Central selections + Vetoes
- **CR2)** CENTRAL + VBF: Central selections + VBF + Vetoes

In each CR folder,

- wjets and zjets: for mc files except for inclusive DY and Wjets
- wjets_htfilter and zjets_htfilter: for inclusive DY and Wjets. We turn on the ht filter from 0 to 100, so that the output file can mimick ht binned from 0 to 100, which we are missing.
- wjets_data and zjets_data: for running data. It is important to note that the output file name should specify the year and the version of the data, i.e. "SingleMuon_2016B.root" 

`run0lep.py` and `batch.py` will automatically do things for you. Just edit the config files as you need them to be.

# SF
From the cutflow output from the Plotter, get scale factors for W or Z for each step.

# PlotterConfig
Config for the Plotter

# run0lep.py
* Inside the `run0lep.py`, change `PartDet` and `year` in line #16-17.
* Then, simply run **`python3 run0lep.py <input file>`**

```shell
# Data
python3 run0lep.py /hdfs/store/data/Run2016C/SingleMuon/NANOAOD/Nano1June2019-v1/30000/F67E58A1-F245-984D-8953-BEB8ECD16B84.root

# TTbar mc sample
python3 run0lep.py /hdfs/store/mc/RunIISummer16NanoAODv6/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/NANOAODSIM/PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v2/20000/7378B9CD-404E-B045-9E05-E261D30BC883.root

# Inclusive WJets mc sample
python3 run0lep.py /hdfs/store/mc/RunIISummer16NanoAODv6/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/NANOAODSIM/PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v1/270000/0F95EA56-FF3C-A940-A3F7-0BABD701D91D.root
```
