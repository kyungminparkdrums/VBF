'''

Save as pdf format the figures from the plotter output root file, applying user options

Run 'python redrawSave.py --guide' for instruction
 
Kyungmin Park (kyungmin.park@cern.ch; jazzykm0110@uos.ac.kr)

'''

import os, sys, getopt
#from ROOT import TFile, TDirectory, TCanvas, TPad, TObject, THStack, TH1D, TAxis, TLegend, TText, TPaveText, TBox, TStyle, gStyle
from ROOT import *

# input file
file_dir = "/home/kyungminpark/CMSSW_10_2_18/src/vbfsusy/plotter/"
if not file_dir.endswith("/"):
    file_dir += "/"

file_name = "test.root"
infile = file_dir+file_name

# output file directory
output_dir = "./output/"
if not output_dir.endswith("/"):
    output_dir += "/"

if not os.path.exists(output_dir):
    os.mkdir(output_dir)
    print("\nCreated the output directory({})\n".format(output_dir))

# name of cut step
step = "NDiMuonCombinations"

# name of kinematics 
kinematic = "DiMuonPt"

# x axis settings
set_logX = False
change_x_range = False
change_x_title = False
x_range = [0, 200]
x_title = "p_{T}(#mu,#mu)"

# y axis settings for the stacked histogram
set_logY = False
change_histo_y_range = False
change_histo_y_title = False
histo_y_range = [0, 400*(10**3)]
histo_y_title = "Events"

# y axis settings for the ratio plot
change_ratio_y_range = False
ratio_y_range = [0.6, 1.4]

# other settings
display_title = False
draw_without_ratio = False
legend_nColumn = 1

isPreliminary = False
status = "Work in Progress"

year_specified = False
lumi = [35.9, 41.5, 59.7]

def replot():
    if os.path.exists(infile):
        f = TFile(infile)
    else:
        print("The file({}) does not exist. Terminating the program.\n".format(infile))
        sys.exit()

    try:
        # Directory of cut step
        stepDir = f.Get(step)

        # Canvas of kinematics
        canvas = stepDir.Get(kinematic)

        # Stacked histogram
        stack_pad = canvas.GetPad(1)
        hs_mc = stack_pad.GetPrimitive(kinematic)

        # Ratio plot
        ratio_pad = canvas.GetPad(2)
        ratio_bar = ratio_pad.GetPrimitive("error_rebin")
    except:
        print("Cannot access the stacked histogram named {} inside the directory {}. Terminating the program.\n".format(kinematic, step))
        sys.exit()

    # Make sure lumi on top right side of the canvas is correct
    if year_specified == True:
        lumi_text = stack_pad.GetListOfPrimitives()[3]
        lumi_text.Clear()
        lumi_text.AddText("{:.1f} fb^{} (13 TeV)".format(lumi[abs(2018-(year+2))],"{-1}"))

    # Work in Progress or Preliminary under CMS logo
    cms_text = stack_pad.GetListOfPrimitives()[5]
    cms_text.Clear()
    cms_text.AddText(status)
    cms_text.SetTextSize(0.04)

    # Legend
    legend = stack_pad.GetListOfPrimitives()[7]
    legend.SetNColumns(legend_nColumn)
    legend.SetTextSize(0.03)
    legend.SetY1(0.3)
    if legend_nColumn > 1:
        legend.SetX1(0.8-legend_nColumn*0.06)
        legend.SetY1(0.5+legend_nColumn*0.06)

    # Change x-axis settings
    if change_x_range == True:
        hs_mc.GetXaxis().SetRangeUser(x_range[0], x_range[1])
        ratio_bar.GetXaxis().SetRangeUser(x_range[0], x_range[1])

    if change_x_title == True:
        ratio_bar.GetXaxis().SetTitle(x_title)

    if set_logX == True:
        stack_pad.SetLogx()
        ratio_pad.SetLogx()

    # Stacked histogram: Change y-axis settings
    # avoid overlap of histogram with the CMS logo
    if set_logX == False:
        hs_mc.SetMaximum(hs_mc.GetMaximum()*1.2)
        if set_logY == True:
            hs_mc.SetMaximum(hs_mc.GetMaximum()*10) 

    if change_histo_y_range == True:
        hs_mc.SetMinimum(histo_y_range[0])
        hs_mc.SetMaximum(histo_y_range[1])

    if change_histo_y_title == True:
        hs_mc.GetYaxis().SetTitle(histo_y_title)
 
    hs_mc.GetYaxis().SetTitleSize(0.04)
    hs_mc.GetYaxis().SetTitleOffset(0.88)

    if set_logY == True:
        stack_pad.SetLogy()

    # Ratio: Change y-axis settings
    if change_ratio_y_range == True:
        ratio_bar.GetYaxis().SetRangeUser(ratio_y_range[0]*0.9, ratio_y_range[1]*1.05)
    
    ratio_bar.GetYaxis().SetTitleSize(0.12)
    ratio_bar.GetYaxis().SetTitleOffset(0.28)

    # Update all changes to the pad/canvas
    stack_pad.Modified()
    stack_pad.Update()

    ratio_pad.Modified()
    ratio_pad.Update()

    canvas.Modified()
    canvas.Update()

    # Save as pdf
    outfile = "{}{}_{}".format(output_dir,step,kinematic)
    
    if display_title == False:
        gStyle.SetOptTitle(0)

    if draw_without_ratio == True:
        hs_mc.GetHistogram().GetXaxis().SetTitle("why not working?")
        stack_pad.SetPad(0,0,1,1)
        stack_pad.Modified()
        stack_pad.Update()
        outfile += "_without_ratio"
        stack_pad.SaveAs("{}.pdf".format(outfile))
    else:
        canvas.SaveAs("{}.pdf".format(outfile))

def printUsage():
    print("\nUsage: python saveFig.py --input_file <root file> --step <cut step> --kinematic <kinematic>")
    print("Additional options you can add are as below: \n--year <year> \n--output_dir <output directory>\n--legend_column <# of columns for legend>\n--display_title <True or False> \n--draw_without_ratio <True or False> \n--set_logX <True or False> \n--x_range <x axis range in list format> \n--x_title <x axis title in TLatex format> \n--set_logY <True or False> \n--histo_y_range <stacked histogram y axis range in list format> \n--histo_y_title <stacked histogram y axis title> \n--ratio_y_range <ratio plot y axis range in list format>\n") 
 

# read the arguments of options and apply those options
try:
    opts,args = getopt.getopt(sys.argv[1:], ":", ["guide=","year=","isPreliminary=","output_dir=","input_file=","step=","kinematic=","legend_column=","display_title=","draw_without_ratio=","set_logX=","x_range=","x_title=","set_logY=","histo_y_range=","histo_y_title=","ratio_y_range="])
except getopt.GetoptError:
    printUsage()
    sys.exit()

hasInput = False
hasStep = False
hasKinematic = False

for opt, arg in opts:
    if opt == "--guide":
        printUsage()
        sys.exit()
    elif opt == "--year":
        year = int(arg)
        year_specified = True
    elif opt == "--isPreliminary":
        isPreliminary = eval(arg)
        if isPreliminary == True:
             status = "Preliminary"
    elif opt == "--output_dir":
        output_dir = arg
    elif opt == "--input_file":
        infile = arg
        hasInput = True
    elif opt == "--step":
        step = arg
        hasStep = True
    elif opt == "--kinematic":
        kinematic = arg
        hasKinematic = True
    elif opt == "--legend_column":
        legend_nColumn = int(arg)
    elif opt == "--display_title":
        display_title = arg
    elif opt == "--draw_without_ratio":
        draw_without_ratio = eval(arg)
    elif opt == "--set_logX":
        set_logX = eval(arg)
    elif opt == "--x_range":
        change_x_range = True
        x_range = eval(arg)
    elif opt == "--x_title":
        change_x_title = True
        x_title = arg
    elif opt == "--set_logY":
        set_logY = eval(arg)
    elif opt == "--histo_y_range":
        change_histo_y_range = True
        histo_y_range = eval(arg)
    elif opt == "--histo_y_title":
        change_histo_y_title = True
        histo_y_title = arg
    elif opt == "--ratio_y_range":
        change_ratio_y_range = True
        ratio_y_range = eval(arg)

if hasInput == False or hasStep == False or hasKinematic == False:
    print("\nMake sure you provided all the mandatory arguments: --input_file <root file> --step <cut step> --kinematic <kinematic>")
    printUsage()
    sys.exit()

# redraw the figure with the given options and save it as pdf
replot()
