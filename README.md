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

# PlotterOutput
Output from the Plotter

- **Root**: output file in root format from the Plotter
- **SaveAsPdf**: reads the output file in root format and save certain figures inside the root file as pdf, following the options given by user
  - **`saveFigures.py`**: Get a plotter output root file and a config file that contains the options for saving the figures from the plotter output. Then, save them as pdf files following the user options given in the config file. `python saveFigures.py --config <config file> --input_file <input root file (output file from the Plotter)>`
  - **config**: i.e. `config/saveOptions.config`
    - Config file contains options for saving figures. 
    - Mandatory options to be included in every line are as follows. ```--step <cut step> --kinematic <kinematic>```
    - Additional options you can add are as follows. ```--output_dir <output directory>\n--display_title <True or False> \n--draw_without_ratio <True or False> \n--set_logX <True or False> \n--x_range <x axis range in list format> \n--x_title <x axis title in TLatex format> \n--set_logY <True or False> \n--histo_y_range <stacked histogram y axis range in list format> \n--histo_y_title <stacked histogram y axis title> \n--ratio_y_range <ratio plot y axis range in list format>\n```


# RunAnalyzer
`python3 run0lep_2016.py [sample]`

# SF
From the cutflow output from the Plotter, get scale factors for W or Z for each step.

`python3 calculateSF.py 2016_Z_CR1_cutflow.txt DY+Jets`

# SamplesXsec
Config for the Plotter

# hadd
hadd/merge outputs
