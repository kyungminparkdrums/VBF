# VBF
for uos gitlab users, 
https://gitlab.sscc.uos.ac.kr/analysis/vbfsusy

# PartDets
Config files for wjets and zjets background estimation, respectively
- **CR1)** CENTRAL: Central selections + Vetoes
- **CR2)** CENTRAL + VBF: Central selections + VBF + Vetoes

In each CR folder,

- wjets and zjets: for mc files except for inclusive DY and Wjets
- wjets_htfilter and zjets_htfilter: for inclusive DY and Wjets. We turn on the ht filter from 0 to 100, so that the output file can mimick ht binned from 0 to 100, which we are missing.
- wjets_data and zjets_data: for running data. It is important to note that the output file name should specify the year and the version of the data, i.e. "SingleMuon_2016B.root" 

**run0lep.py** and **batch_201*.py** will automatically do these for you. Just edit the config files as you need them to be.

