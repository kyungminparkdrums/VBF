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

- **`Root`** folder: contains output files in root format from the Plotter
- **`SaveAsPdf`** folder: reads the output file in root format and save certain figures inside the root file as pdf, following the options given by user
  - **`saveFigures.py`**: Get a plotter output root file and a config file that contains the options for saving the figures from the plotter output. Then, save them as pdf files following the user options given in the config file. 
      ```
         python saveFigures.py --config <config file> --input_file <input root file (output file from the Plotter)>
      ```
  - Running the line above will give you the certain histograms after certain cut step that you specified in the config file, in pdf format under the name of `<cut_step>_<histogram_name>.pdf`. Unless you specified the output pdf directory in the config file, i.e. `--output_dir <dir>`, these will be stored in `./output/` directory which will be automatically created.
  - **config**: i.e. `config/saveOptions.config`
    - Config file contains options for saving figures. 
    - Mandatory options to be included in every line are as follows. 
      ```
         --step <cut step> --kinematic <kinematic>
      ```
    - Additional options you can add are as follows. 
      ```
         --output_dir <output directory>
         --display_title <True or False>
         --draw_without_ratio <True or False>
         --set_logX <True or False>
         --x_range <x axis range in list format> 
         --x_title <x axis title in TLatex format>
         --set_logY <True or False> 
         --histo_y_range <stacked histogram y axis range in list format> 
         --histo_y_title <stacked histogram y axis title>
         --ratio_y_range <ratio plot y axis range in list format>
      ```
    - IMPORTANT: when giving options for axis title, please note the followings (otherwise, it'll crash):
      - 1. if the title contains brackets, please put a backslash before opening and closing of the brackets, i.e. `p_{T}\(jj\)` instead of `p_{T}(jj)`
      - 2. if the title contains greek letters that require backslash in latex form, replace the backslash with hashtag, i.e. `#mu` instead of `\mu`
      ```
      # Example
      --step NDiMuonCombinations --kinematic DiMuonPt --ratio_y_range [0.6,1.4] --x_range [0,300]
      --step NRecoTriggers1 --kinematic Met --set_logY True --x_title p^{miss}_{T}[GeV]
      ```

```
# Example
# from /VBF/PlotterOutput/, 
cd ./SaveAsPdf/
python saveFigures.py --config ./config/saveOptions.config --input_file ../Root/2016_Z_CR2.root

```

# RunAnalyzer
`python3 run0lep_2016.py [sample]`

# SF
From the cutflow output from the Plotter, get scale factors for W or Z for each step.

`python3 calculateSF.py 2016_Z_CR1_cutflow.txt DY+Jets`

# SamplesXsec
Config for the Plotter

# hadd
hadd/merge outputs
