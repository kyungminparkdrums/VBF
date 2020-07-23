# VBF
for uos gitlab users, 
https://gitlab.sscc.uos.ac.kr/analysis/vbfsusy

# PartDets
Config files for wjets and zjets background estimation, respectively
- **CR1)** CENTRAL: Central selections + Vetoes
- **CR2)** CENTRAL + VBF: Central selections + VBF + Vetoes

In every CR,

- wjets and zjets: for mc files except for inclusive DY and Wjets
- wjets_htfilter and zjets_htfilter: for inclusive DY and Wjets. We turn on the ht filter from 0 to 100, so that the output file can mimick ht binned from 0 to 100, which we are missing.
- wjets_data and zjets_data: for running data. It is important to note that the output file name should specify the year and the version of the data, i.e. "SingleMuon_2016B.root" 

**run0lep.py** and **batch.py** will automatically do these for you. Just edit the config files as you need them to be.


As of July 10 2020, the config files follow the AN 2017_026_v18, except for these below.
1. Muon Eta range 2.1 (instead of 2.5): for better efficiencies
2. Muon Iso 0.15 (instead of 0.25)
3. Deep tau id  
4. Deep csv for bjets
5. Jet Overlap removal is added with delta R size 0.4
6. DiMuon Charge Cut is applied


# batch.py and run0lep.py
This is for gate.sscc.uos.ac.kr users.


