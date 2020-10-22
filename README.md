# Batch
Batch submitting code (2016 - 2018) with `run0lep.py` and `hadoopCondorSubmit.py` in UOS gate server

# PartDets
Config files for wjets and zjets background estimation, respectively
- **CR1)** CENTRAL: Central selections + Vetoes
- **CR2)** CENTRAL + VBF: Central selections + VBF + Vetoes

In each CR folder,

- wjets and zjets: for mc files except for inclusive DY and Wjets
- wjets_htfilter and zjets_htfilter: for inclusive DY and Wjets. We turn on the ht filter from 0 to 100, so that the output file can mimick ht binned from 0 to 100, which we are missing.
- wjets_data and zjets_data: for running data. It is important to note that the output file name should specify the year and the version of the data, i.e. "SingleMuon_2016B.root" 

`run0lep.py` and `batch.py` will automatically do things for you. Just edit the config files as you need them to be.

# RunAnalyzer
`python3 run0lep_2016.py [sample]`

# SF
From the cutflow output from the Plotter, get scale factors for W or Z for each step.

`python3 calculateSF.py 2016_Z_CR1_cutflow.txt DY+Jets`

# SamplesXsec
Config for the Plotter

# hadd
hadd/merge outputs
