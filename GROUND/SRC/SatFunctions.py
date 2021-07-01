


##
## Name          : .py
## Purpose       : Receiver Sensor Analyses 
## Project       : Vicinity
## Component     : Miguel
## Author        : Vicinity
## Creation date : 2021/06/05
## File Version  : 1.0
## Version date  : 2021/06/05
##



import sys, os
from pandas import unique
from interfaces import INPUT_IDX
sys.path.append(os.getcwd() + '/' + \
    os.path.dirname(sys.argv[0]) + '/' + 'COMMON')

from COMMON.Plots import generatePlot
import numpy as np
import math
# from pyproj import Transformer
from COMMON.Coordinates import xyz2llh


# plotNameOfTheFunction
def plotNameOfTheFunction(InputData):
    # Initialize scenario to store plot properties
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (8.4,6.6)
    PlotConf["Title"] = " "

    PlotConf["yLabel"] = ""


    PlotConf["xLabel"] = ""
    PlotConf["xTicks"] = 
    PlotConf["xLim"] = [0, 24]

    PlotConf["Grid"] = 1

    PlotConf["Marker"] = '|'

    PlotConf["ColorBar"] = "gnuplot"
    PlotConf["ColorBarLabel"] = ""
    PlotConf["ColorBarMin"] = 0.
    PlotConf["ColorBarMax"] = 90.

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}
    PlotConf["zData"] = {}

    PlotConf["xData"][Label] = InputData[INPUT_IDX

    PlotConf["yData"][Label] = InputData[INPUT_IDX
    
    PlotConf["zData"][Label] = InputData[INPUT_IDX

    PlotConf["Path"] = sys.argv[1] + '/OUT/' + 'plotNameOfTheFunction'

    # Call generatePlot from Plots library
    generatePlot(PlotConf)

