# pyinnovativetrend

Trend analysis is a statistical technique used to examine data over time to identify patterns, trends, or movements in a particular direction. It is widely used in various fields such as finance, economics, marketing, environmental science, and many others. A very common and conventional method to detect trend is mann-kendall trend test proposed by Mann and Kendall. However, an innovative method, proposed by Sen (2012), is widely used now-a-days due to its simplicity and graphical features. This innovative trend analysis method is very sensitive and can detect trends that are overlooked by conventional methods like MK test.


## Installation
The package is installed using pip:

    pip install pyinnovativetrend

## Function details:
### pyinnovativetrend.ITA_single
**pyinnovativetrend.ITA_single( x, length, alpha = 0.05, graph={}, showgraph = True)**\
This function calculates trend and other necessary parameters for single list or numpy array and returns a named tuple. By default, a graph is illustrated and saved on the local machine.\
Example:

    import pyinnovativetrend as pit
    x = [1,2,3,4,5,6,2,3,5,2,3,4,4]
    graph ={
        'xlabel' : 'First sub-series (1980 - 1985)',
        'ylabel' : 'Second sub-series (1986 - 1991)',
        'title' : 'Time series analysis',
        'dpi' : 450,
        'fontsize' : 10
    }

    pit.ITA_single(x, 12, graph = graph)


Output:
ITA(trend='No trend', h=False, p=0.2049477839420626, z=-1.2675805428826508, slope=-0.027777777777777752, standard_deviation=1.2555432644432805, slope_standard_deviation=0.021914014011770254, correlation=0.9341987329938274, lower_critical_level=-0.0429506782197758, uper_critical_level=0.0429506782197758)

![Single trend analysis](/outputfig.png)

## pyinnovativetrend.ITA_multiple_by_station
**ITA_multiple_by_station(length, filename=[], column=[], exceptcolumn=[],graph={}, alpha =0.05, rnd=2, csv = False, directory_path = "./", output=[], out_direc="./")**\
This function calculates trend and other necessary parameters for multiple stations. The data is retrieved from excel or csv files from a desired or root directory and results are saved as excel format sorted by stations on desired or root directory. By default, multiple graphs sorted by stations are illustrated and saved on the local machine on desired directory or root directory.\
Example:

    import pyinnovativetrend as pit
    graph ={
        'xlabel' : 'First sub-series (1980 - 1985)',
        'ylabel' : 'Second sub-series (1986 - 1991)',
        'title' : 'Time series analysis',
        'dpi' : 450,
        'fontsize' : 10
    }

    pit.ITA_multiple_by_station(38, exceptcolumn=['Year'], graph = graph)


Output:\
Excel files sample
![Single trend analysis](/barisalExcel.png)
Figure Sample
![Single trend analysis](/Barisal.png)
## pyinnovativetrend.ITA_multiple_by_column
**pyinnovativetrend.ITA_multiple_by_station (length, filename=[], column=[], exceptcolumn=[],graph={}, alpha =0.05, rnd=2, csv = False, directory_path = "./", output=[], out_direc="./")**\
This function calculates trend and other necessary parameters for multiple stations. The data is retrieved from excel or csv files from a desired or root directory and results are saved as excel format sorted by columns on desired or root directory. By default, multiple graphs sorted by columns are illustrated and saved on the local machine on desired directory or root directory.\
Example:

    import pyinnovativetrend as pit
    graph ={
        'xlabel' : 'First sub-series (1980 - 1985)',
        'ylabel' : 'Second sub-series (1986 - 1991)',
        'title' : 'Time series analysis',
        'dpi' : 450,
        'fontsize' : 10
    }

    pit.ITA_multiple_by_column(38, exceptcolumn=['Year'], graph = graph)


Output:\
Excel files sample
![Single trend analysis](/postmonsoonexcel.png)
Figure Sample
![Single trend analysis](/Post-Monsoon.png)

### pyinnovativetrend.ITA_single_vis(x,length,graph={})
**pyinnovativetrend.ITA_single_vis(x,length,figsize=(10,10),graph={})**\
This function illustrates a graph and saves on the local machine.\

Example:

    import pyinnovativetrend as pit
    x = [1,2,3,4,5,6,2,3,5,2,3,4,4]
    graph ={
        'xlabel' : 'First sub-series (1980 - 1985)',
        'ylabel' : 'Second sub-series (1986 - 1991)',
        'title' : 'Time series analysis',
        'dpi' : 450,
        'fontsize' : 10
    }

    pit.ITA_single_vis(x, 12, graph = graph)


Output:

![Single trend analysis](/outputfig.png)

### pyinnovativetrend.ITA_multiple_vis_by_station
**pyinnovativetrend.ITA_multiple_vis_by_station(length, graph={}, filename=[], column=[], exceptcolumn=[], csv = False, directory_path = "./")**\
This function illustrates multiple graphs sorted by stations and saves on the local machine on desired directory or root directory. The data is retrieved from excel or csv files from a desired or root directory and results are saved as excel format sorted by stations on desired or root directory.
Example:

    import pyinnovativetrend as pit
    graph ={
        'xlabel' : 'First sub-series (1980 - 1985)',
        'ylabel' : 'Second sub-series (1986 - 1991)',
        'title' : 'Time series analysis',
        'dpi' : 450,
        'fontsize' : 10
    }

    pit.ITA_multiple_vis_by_stations(38, exceptcolumn=['Year'], graph = graph)


Output:

![Single trend analysis](/Barisal.png)

### pyinnovativetrend.ITA_multiple_vis_by_column
**pyinnovativetrend.ITA_multiple_vis_by_column(length, graph={}, filename=[], column=[], exceptcolumn=[], csv = False, directory_path = "./")**\
This function illustrates multiple graphs sorted by stations and saves on the local machine on desired directory or root directory. The data is retrieved from excel or csv files from a desired or root directory and results are saved as excel format sorted by columns on desired or root directory.
Example:

    import pyinnovativetrend as pit
    graph ={
        'xlabel' : 'First sub-series (1980 - 1985)',
        'ylabel' : 'Second sub-series (1986 - 1991)',
        'title' : 'Time series analysis',
        'dpi' : 450,
        'fontsize' : 10
    }

    pit.ITA_multiple_vis_by_stations(38, exceptcolumn=['Year'], graph = graph)


Output:

![Single trend analysis](/Post-Monsoon.png)

The function takes a list or numpy array and calculates trend using innovative trend analysis method. 
### Parameters:
**x : List or numpy array**\
The time series or data series whose trend is to be determined

**length : integer**\
Length of the time series. If given length of the time series is odd, the earliest/first entry will be ommitted.

**filename : List default all excel/csv files**\
List of files or stations which contain the data sorted by month/year/season.

**column : List default all columns**\
List of columns or data-series which contain the data.

**exceptcolumn : List default empty list**\
List of columns for which analysis is not required (For example, column of year).

**csv : bool default False**
The type of files. By default the file type is excel. However, if the files are in csv format, csv should be assigned to True.

**directory_path : string default root**\
Directory path of the files where the files are stored.

**output : list default station names or column names**\
Name of the files by which the results will be saved.

**out_direc : string default root**\
Directory path of the files where the results will be saved.

**alpha : float default 0.05**\
Level of significance in a two-tailed test.

**showgraph : bool default True**\
Choose if graph is to be illustrated along with calculation in single analysis.

**graph : python dictionary (optional)**
**Default values**
'trendLineStyle' : 'dashed'      # Line style of trend line, for more line style type visit documentation of matplotlib\
'scatterMarker' : '.'            # Marker type of scattered data points, for more marker visit documentation of matplotlib\
'title' : ''                     # Title of the graph or illustration\
'xlabel' : 'First sub-series'    # Label of X-axis\
'ylabel' : 'Second sub-series'   # Label of Y-axis\
'noTrendLineStyle' : 'solid'     # Line style of no trend line or 1:1 line, for more line style type visit documentation of matplotlib\
'output_dir' : './'              # Directory of output file where graph is to be saved\
'output_name' : 'outputfig.png'  # Name of the graph or illustration\
'dpi' : 300                      # Dot per inch (dpi) of the graph or illustration\
'row' : -                        # Row number of the subplots. If not provided, will be calculated automatically. (Available only for multiple analysis)\
'colm': -                        # column number of the subplots. If not provided, will be calculated automatically. (Available only for multiple analysis)\

