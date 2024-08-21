# pyinnovativetrend

Trend analysis is a statistical technique used to examine data over time to identify patterns, trends, or movements in a particular direction. It is widely used in various fields such as finance, economics, marketing, environmental science, and many others. A very common and conventional method to detect trend is mann-kendall trend test proposed by Mann and Kendall. However, an innovative method, proposed by Sen (2012), is widely used now-a-days due to its simplicity and graphical features. This innovative trend analysis method is very sensitive and can detect trends that are overlooked by conventional methods like MK test.


## Installation
The package is installed using pip:

    pip install pyinnovativetrend

## Function details:
### pyinnovativetrend.ITA_single
**pyinnovativetrend.ITA_single(x, length, alpha = 0.05, figsize=(10,10), graph={})**

Example:

    import pyinnovativetrend as pit
    x = [1,2,3,4,5,6,2,3,5,2,3,4,4]
    graph ={
        'xlabel' : 'First sub-series (1980 - 1985)',
        'ylabel' : 'Second sub-series (1986 - 1991),
        'title' : 'Time series analysis',
        'dpi' : 450
    }

    pit.ITA_single(x, 12, graph = graph)


Output:
ITA(trend='No trend', h=False, p=0.2049477839420626, z=-1.2675805428826508, slope=-0.027777777777777752, standard_deviation=1.2555432644432805, slope_standard_deviation=0.021914014011770254, correlation=0.9341987329938274, lower_critical_level=-0.0429506782197758, uper_critical_level=0.0429506782197758)

![Single trend analysis](/outputfig.png)

## pyinnovativetrend.ITA_multiple_by_station 
**pyinnovativetrend.ITA_multiple_by_station (length, filename=[], column=[], exceptcolumn=[],graph={}, alpha =0.05, rnd=2, csv = False, directory_path = "./", output=[], out_direc="./")**

<h3>pyinnovativetrend.ITA_multiple_by_column </h3>
<b>pyinnovativetrend.ITA_multiple_by_column(length, filename=[], column=[], exceptcolumn=[],graph={}, alpha =0.05, rnd=2, csv = False, directory_path = "./", output=[], out_direc="./") </b>

<h3>pyinnovativetrend.ITA_single_vis() </h3>
<b>pyinnovativetrend.ITA_single_vis(x,length,figsize=(10,10),graph={}) </b>

<h3>pyinnovativetrend.ITA_multiple_vis_by_station() </h3>
<b>pyinnovativetrend.ITA_multiple_vis_by_station(length, graph={}, filename=[], column=[], exceptcolumn=[], csv = False, directory_path = "./")</b>

<h3>pyinnovativetrend.ITA_multiple_vis_by_column() </h3>
<b> pyinnovativetrend.ITA_multiple_vis_by_column(length, graph={}, filename=[], column=[], exceptcolumn=[], csv = False, directory_path = "./") </b>

The function takes a list or numpy array and calculates trend using innovative trend analysis method. 
<h4 style="background-color:powderblue;"> Parameters: </h4>
<b> x : List or numpy array </b> </br>
The time series or data series whose trend is to be determined

<b> length : integer </b></br>
Length of the time series. If given length of the time series is odd, the earliest/first entry will be ommitted.

<b> filename : List default all excel/csv files</b></br>
List of files or stations which contain the data sorted by month/year/season.

<b> column : List default all columns </b></br>
List of columns or data-series which contain the data.

<b> exceptcolumn : List default empty list</b></br>
List of columns for which analysis is not required (For example, column of year).

<b> csv : bool default False </b></br>
The type of files. By default the file type is excel. However, if the files are in csv format, csv should be assigned to True.

<b> directory_path : string default root </b></br>
Directory path of the files where the files are stored.

<b> output : list default station names or column names</b></br>
Name of the files by which the results will be saved.

<b> out_direc : string default root </b></br>
Directory path of the files where the results will be saved.

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
'row' : -                        # Row number of the subplots. If not provided, will be calculated automatically. (Available only for multiple analysis) </br>
'colm': -                        # column number of the subplots. If not provided, will be calculated automatically. (Available only for multiple analysis) </br>

