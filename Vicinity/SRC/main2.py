

##
## Name          : main2receiver_analysis.py
## Purpose       : Receiver Sensor Analyses 
## Project       : Vicinity
## Component     : Miguel
## Author        : Vicinity
## Creation date : 2021/06/05
## File Version  : 1.0
## Version date  : 2021/06/05
##



import sys, os
from collections import OrderedDict
from interfaces import INPUT_IDX
from pandas import read_csv
from yaml import dump




def displayUsage():
    sys.stderr.write("ERROR: Please provide path to SCENARIO as a unique \nargument\n")

def readConf(CfgFile):
    Conf = OrderedDict({})
    with open(CfgFile, 'r') as f:
        # Read file
        Lines = f.readlines()

        # Read each configuration parameter which is compound of a key and a value
        for Line in Lines:
            if "#" in Line: continue
            LineSplit = Line.split('=')
            try:
                LineSplit = list(filter(None, LineSplit))
                Conf[LineSplit[0].strip()] = LineSplit[1].strip()

            except:
                sys.stderr.write("ERROR: Bad line in conf: %s\n" % Line)

    return Conf



if len(sys.argv) != 2:
    displayUsage()
    sys.exit()

# Take the arguments
Mission = sys.argv[1]

# Path to conf
CfgFile = Mission + '/CFG/ajustes.cfg'

# Read conf file
Conf = readConf(CfgFile)
print(dump(Conf))

# Get Inputs file path
#InputFile = Mission + '/INP' + Conf["nameOfTheInputFile"] ##OJO

if(Conf["PLOT_NAME1"]):
    # Read the cols we need from Input file
    InputData = read_csv(InputFile, delim_whitespace=True, skiprows=1, header=None,\
    usecols=[INPUT_IDX["SOD"]])#,INPUT_IDX[""],INPUT_IDX[""]])
    
    # Configure plot and call plot generation function
    SatFunctions.plotNameOfTheFunction(InputData)