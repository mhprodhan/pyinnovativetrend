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
** x : List or numpy array **
The time series or data series whose trend is to be determined

** length : integer **
Length of the time series. If given length of the time series is odd, the earliest/first entry will be ommitted. **

** alpha : float default 0.05 **
Level of significance in a two-tailed test.

** graph : python dictionary,  **
