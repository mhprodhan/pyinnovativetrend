# pyinnovativetrend

Trend analysis is a statistical technique used to examine data over time to identify patterns, trends, or movements in a particular direction. It is widely used in various fields such as finance, economics, marketing, environmental science, and many others. A very common and conventional method to detect trend is mann-kendall trend test proposed by Mann and Kendall. However, an innovative method, proposed by Sen (2012), is widely used now-a-days due to its simplicity and graphical features. This innovative trend analysis method is very sensitive and can detect trends that are overlooked by conventional methods like MK test.


## Installation
The package is installed using pip:

    pip install pyinnovativetrend

## Function details:
### pyinnovativetrend.ITA_single(x, length, alpha = 0.05, graph={})
### pyinnovativetrend.ITA_multiple_by_station ()
### pyinnovativetrend.ITA_multiple_by_column ()
### pyinnovativetrend.ITA_single_vis()
### pyinnovativetrend.ITA_multiple_vis_by_station()
### pyinnovativetrend.ITA_multiple_vis_by_column()

The function takes a list or numpy array and calculates trend using innovative trend analysis method. 
<h4 style="background-color:powderblue;"> Parameters: </h4>
<b> x : List or numpy array </b> </br>
The time series or data series whose trend is to be determined

<b> length : integer </b></br>
Length of the time series. If given length of the time series is odd, the earliest/first entry will be ommitted. **

<b> alpha : float default 0.05 </b></br>
Level of significance in a two-tailed test.

<b> graph : python dictionary (optional) </b></br>
<i>Default values </i></br>
'trendLineStyle' : 'dashed'      # Line style of trend line, for more line style type visit documentation of matplotlib.</br>
'scatterMarker' : '.'            # Marker type of scattered data points, for more marker visit documentation of matplotlib</br>
'title' : ''                     # Title of the graph or illustration.</br>
'xlabel' : 'First sub-series'    # Label of X-axis</br>
'ylabel' : 'Second sub-series'   # Label of Y-axis</br>
'noTrendLineStyle' : 'solid'     # Line style of no trend line or 1:1 line, for more line style type visit documentation of matplotlib. </br>
'output_dir' : './'              # Directory of output file where graph is to be saved.</br>
'output_name' : 'outputfig.png'  # Name of the graph or illustration.</br>
'dpi' : 300                      # Dot per inch (dpi) of the graph or illustration.</br>

