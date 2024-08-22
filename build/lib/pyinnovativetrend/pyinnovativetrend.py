
import numpy as np
from math import sqrt
from collections import namedtuple
import os
import pandas as pd
from .visualization import *
from .util  import *
     


def ITA_single(x, length, alpha = 0.05, graph={}, showgraph = True):
    """
    This method, proposed by Sen (2012), is used to estimate the magnitude of the trend. 
    Input:
        x:   a one dimensional vector (list, numpy array or pandas series) data
        length: length of the dataseries whose trend is to be determined
        graph (optional): the array with the properties of visualization
        figsize (optional): the figsize of the graph that will be visualized, by default value is (10,10)
        alpha (optional): level of significance, by default 5% significance level is selected

    Output:
        trend: tells if trend exists and type of trend
        h: True (if trend is present) and False (if trend is absent)
        p: p-value for the significant test (2-tailed test)
        z: normalized test statistics (2-tailed test)
        slope: slope of the trend
        standard_deviation: standard deviation of the data series
        slope_standard_deviation: standard deviation of slope
        correlation: correlation between the sorted sub-series
        lower_critical_level: lower critical value for 2-tailed test
        upper_critical_level: upper critical value for 2-tailed test
    Examples
    --------
	  >>> import pyinnovativetrend as pit
      >>> x = np.random.rand(120)
      >>> result = pit.ITA_single(x, 120)
    """
    
    #Processed data and length of the data series
    x, n = preprocessing (x,length)
    
    #dividing the data series into two equal sub-series and sorting the sub-series
    fh, sh=np.sort(x[0:n//2]), np.sort(x[n//2:n])
    
    # calculation of slope, standard deviation and correlation between sub-series
    s, sd, corr=2*(np.mean(sh)-np.mean(fh))/n, np.std(x), cor(fh,sh)
    
    #calculation of standard deviation of slope
    ssd = sqrt(8)/sqrt(n**3)*sd*sqrt(1-corr)
    
    #calculation of lower critical level and upper critical level and p_value for the data series
    lcl, ucl, = -p2z(alpha)*ssd, p2z(alpha)*ssd
    p_value, h, trend = z2p(s/ssd,alpha)
    
    res = namedtuple('ITA', ['trend', 'h', 'p', 'z', 'slope', 'standard_deviation', 'slope_standard_deviation','correlation','lower_critical_level','uper_critical_level'])
    if showgraph:
        ITA_single_vis(x, length, graph = graph)
    return res (trend, h, p_value, s/ssd, s, sd, ssd, corr, lcl, ucl)


def ITA_multiple_by_station(length, filename=[], column=[], exceptcolumn=[],graph={}, alpha =0.05, rnd=2, csv = False, directory_path = "./", output=[], out_direc="./"):
    
    """
    This method, proposed by Sen (2012), is used to estimate the magnitude of the trend of multiple stations with multiple data series. The results and graphs will be arranged by stations and saved in the folder. 
    Input:
        length: length of the dataseries whose trend is to be determined
        filename (optional): the name of the selected files, by default select all files in the given folder
        column (optional): the name of the columns of the stations, by default select all columns
        exceptcolumn (optional): the list of the coumns which will be eliminated, by default select no columns
        graph (optional): the array with the properties of visualization
        alpha (optional): level of significance, by default 5% significance level is selected
        rnd (optional): rounding of the results, by default every result is rounded upto 2 decimal points except p-value (rounded upto 3 decimal points)
        csv (optional): if the files in csv format, by default files are in excel format
        directory_path (optional): the directory path of the files, by default root path is selected
        output (optional): the list of the names of the output files, by default the the output files will assume name of the stations
        out_direc (optional): the directory of the output files, by default output files will be saved at the root folder.

    Output:
        

    Examples
    --------
	  >>> import pyinnovativetrend as pit
      >>>  exceptcolumn=['Year']
      >>>  graph={
            'xlabel' : 'First half sub-series (1983-2002)',
            'ylabel' : 'Second half sub-series (2003-2022)',
            'title' : 'ITA by stations'
            }

      >>> result = pit.ITA_multiple_by_station(40, graph = graph )
    """
    if len(filename) == 0:
        
        if csv:
            filename = [i for i in os.listdir(directory_path) if i.endswith(".csv")]
        
        else:
            filename = [i for i in os.listdir(directory_path) if i.endswith(".xlsx")]
        
        if len(filename) == 0:
            raise Exception("Required files are missing!")
    
    if len(output) == 0:
        
        for file in filename:
            if csv:
                output.append(file[:-4]+"output.xlsx")
                
            else:
                output.append(file[:-5]+"output.xlsx")
    
    if csv:
        x = pd.read_csv(directory_path+filename[0])
        
    else:
        x = pd.read_excel(directory_path+filename[0])
    
    if len(column) == 0:
        column = list(x.columns)
        
        for i in column:
            if i in exceptcolumn:
                column.remove(i)
        
        if len(column) == 0:
            raise Exception("No data series is selected!")
    
    count =0
    for file in filename:
        masterdict = {"Column":[],"Trend":[],"h":[],"P-value":[],"Z score":[],"Slope":[],"Standard Deviation":[],"Slope Standard Deviation":[],"Correlation":[],"Upper Critical Limit":[],"Lower Critical Limit":[]}
        
        for col in column:
            masterdict["Column"].append(col)
            
            if csv:
                x = list(pd.read_csv(directory_path+file)[col])
        
            else:
                x = list(pd.read_excel(directory_path+file)[col])
            
            t, h, p, z, s, sd, ssd, corr, lcl, ucl = ITA_single(x,length,alpha, showgraph = False)
            p, z, s, sd, ssd, corr, lcl, ucl = round(p,3), round(z,rnd), round(s,rnd), round(sd,rnd), round(ssd,rnd), round(corr,rnd), round(lcl,rnd), round(ucl,rnd)
            masterdict["Trend"].append(t); masterdict["h"].append(h); masterdict["P-value"].append(p); masterdict["Z score"].append(z); masterdict["Slope"].append(s); masterdict["Standard Deviation"].append(sd)
            masterdict["Slope Standard Deviation"].append(ssd); masterdict["Correlation"].append(corr); masterdict["Lower Critical Limit"].append(lcl); masterdict["Upper Critical Limit"].append(ucl)
        pd.DataFrame(masterdict).to_excel(out_direc+output[count], index=False)
        
        count += 1
    ITA_multiple_vis_by_station(length, graph=graph,directory_path=directory_path,csv=csv,filename=filename,column=column,exceptcolumn=exceptcolumn)



def ITA_multiple_by_column(length, filename=[], column=[], exceptcolumn=[],graph={}, alpha =0.05, rnd=2, csv = False, directory_path = "./", output=[], out_direc="./"):
    
    """
    This method, proposed by Sen (2012), is used to estimate the magnitude of the trend of multiple stations with multiple data series. The results and graphs will be arranged by columns/dataseries and saved in the folder. 
    Input:
        length: length of the dataseries whose trend is to be determined
        filename (optional): the name of the selected files, by default select all files in the given folder
        column (optional): the name of the columns of the stations, by default select all columns
        exceptcolumn (optional): the list of the coumns which will be eliminated, by default select no columns
        graph (optional): the array with the properties of visualization
        alpha (optional): level of significance, by default 5% significance level is selected
        rnd (optional): rounding of the results, by default every result is rounded upto 2 decimal points except p-value (rounded upto 3 decimal points)
        csv (optional): if the files in csv format, by default files are in excel format
        directory_path (optional): the directory path of the files, by default root path is selected
        output (optional): the list of the names of the output files, by default the the output files will assume name of the stations
        out_direc (optional): the directory of the output files, by default output files will be saved at the root folder.

    Output:
        

    Examples
    --------
	  >>> import pyinnovativetrend as pit
      >>>  exceptcolumn=['Year']
      >>>  graph={
            'xlabel' : 'First half sub-series (1983-2002)',
            'ylabel' : 'Second half sub-series (2003-2022)',
            'title' : 'ITA by stations'
            }

      >>> result = pit.ITA_multiple_by_column(40, graph = graph )
    """
    
    if len(filename) == 0:
        
        if csv:
            filename = [i for i in os.listdir(directory_path) if i.endswith(".csv")]
        
        else:
            filename = [i for i in os.listdir(directory_path) if i.endswith(".xlsx")]
        
        if len(filename) == 0:
            raise Exception("Required files are missing!")
    
    if csv:
        x = pd.read_csv(directory_path + filename[0])
        
    else:
        x = pd.read_excel(directory_path + filename[0])
    
    if len(column) == 0:
        column = list(x.columns)
        
        for i in column:
            if i in exceptcolumn:
                column.remove(i)
        
        if len(column) == 0:
            raise Exception("No data series is selected!")
    
    if len(output) == 0:
        
        for col in column:
            if csv:
                output.append(str(col)+"output.xlsx")
                
            else:
                output.append(str(col)+"output.xlsx")
    
    count =0
    for col in column:
        masterdict = {"Stations":[],"Trend":[],"h":[],"P-value":[],"Z score":[],"Slope":[],"Standard Deviation":[],"Slope Standard Deviation":[],"Correlation":[],"Upper Critical Limit":[],"Lower Critical Limit":[]}
        
        for file in filename:
            if csv:
                masterdict["Stations"].append(file[:-4])
            
            else:
                masterdict["Stations"].append(file[:-5])
            
            if csv:
                x = list(pd.read_csv(directory_path + file)[col])
        
            else:
                x = list(pd.read_excel(directory_path + file)[col])
              
            t, h, p, z, s, sd, ssd, corr, lcl, ucl = ITA_single(x,length,alpha, showgraph=False)
            p, z, s, sd, ssd, corr, lcl, ucl = round(p,3), round(z,rnd), round(s,rnd), round(sd,rnd), round(ssd,rnd), round(corr,rnd), round(lcl,rnd), round(ucl,rnd)
            masterdict["Trend"].append(t); masterdict["h"].append(h); masterdict["P-value"].append(p); masterdict["Z score"].append(z); masterdict["Slope"].append(s); masterdict["Standard Deviation"].append(sd)
            masterdict["Slope Standard Deviation"].append(ssd); masterdict["Correlation"].append(corr); masterdict["Lower Critical Limit"].append(lcl); masterdict["Upper Critical Limit"].append(ucl)
        
        pd.DataFrame(masterdict).to_excel(out_direc+output[count], index=False)
        count += 1
    ITA_multiple_vis_by_column(length, graph=graph,filename=filename,column=column,csv=csv, directory_path=directory_path, exceptcolumn=exceptcolumn)
