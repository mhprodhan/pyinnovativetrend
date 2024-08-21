import numpy as np
import  os
from math import floor,ceil
import pandas as pd
import matplotlib.pyplot as plt
from .util import *

def ITA_single_vis(x,length,figsize=(10,10),graph={}):
    x, length = preprocessing(x,length)
    fh,sh=np.array(x[:length//2]),np.array(x[length//2:])
    fh.sort()
    sh.sort()
    maximum=max(max(fh),max(sh))
    minimum=min(min(fh),min(sh))
    gap = (maximum-minimum)/2
    maximum = (maximum//gap)*gap+gap
    minimum = ((minimum//gap)*gap)
    a=[minimum,maximum]
    m=np.mean(fh)
    M=np.mean(sh)
    if m>M:
        y1=minimum
        x1=minimum+m-M
        x2=maximum
        y2=maximum-m+M
    else:
        y1=minimum+M-m
        x1=minimum
        y2=maximum
        x2=maximum-M+m
    
    plt.figure(figsize=figsize)
    plt.plot([x1,x2],[y1,y2], linestyle=graph.get("trendLineStyle","dashed"))
    plt.scatter(fh,sh,marker=graph.get('scatterMarker','.'))
    plt.title(graph.get('title',""))
    plt.xlabel(graph.get('xlabel',"First sub-series"),fontsize=graph.get('fontsize',(figsize[0]*figsize[1])**0.5))
    plt.ylabel(graph.get('ylabel',"Second sub-series"),fontsize=graph.get('fontsize',(figsize[0]*figsize[1])**0.5))
    plt.plot(a,a,linestyle=graph.get('noTrendLineStyle','solid'))
    plt.tight_layout()
    plt.savefig(graph.get('output_dir','./')+graph.get('output_name','outputfig.png'),dpi=graph.get('dpi',300))
    plt.show()
    

def ITA_multiple_vis_by_station(length, graph={}, filename=[], column=[], exceptcolumn=[], csv = False, directory_path = "./"):
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
    
    row = graph.get('row', floor(len(column)**0.5))
    colm = graph.get('colm', ceil(len(column)/row))

    for file in filename:
        fig,ax=plt.subplots(row, colm, figsize=graph.get('figsize',(colm*7,row*5)))
        count=0
        if csv:
            name = file[:-4]
        
        else:
            name = file[:-5]
        for col in column:
            if csv:
                x = list(pd.read_csv(directory_path+file)[col])
        
            else:
                x = list(pd.read_excel(directory_path+file)[col])

            x, length = preprocessing(x,length)
            fh,sh=np.array(x[:length//2]),np.array(x[length//2:])
            fh.sort()
            sh.sort()
            # print(fh,sh)
            maximum=max(max(fh),max(sh))
            minimum=min(min(fh),min(sh))
            gap = (maximum - minimum)/4
            maximum = (maximum//gap)*gap+gap
            minimum = ((minimum//gap)*gap)
            a=[minimum,maximum]
            m=np.mean(fh)
            M=np.mean(sh)
            if m>M:
                y1=minimum
                x1=minimum+m-M
                x2=maximum
                y2=maximum-m+M
            else:
                y1=minimum+M-m
                x1=minimum
                y2=maximum
                x2=maximum-M+m
            if row > 1:
                ax[count//colm,count%colm].plot([x1,x2],[y1,y2], linestyle=graph.get('trendLineStyle','dashed'))
                ax[count//colm,count%colm].set_yticks(np.arange(minimum,maximum+gap+1,gap))
                ax[count//colm,count%colm].set_xticks(np.arange(minimum,maximum+gap+1,gap))
                ax[count//colm,count%colm].scatter(fh,sh, marker=graph.get("scatterMarker",'.'))
                ax[count//colm][count%colm].plot(a,a)
                ax[count//colm][count%colm].set_title(col)
                

            else:
                ax[count].plot([x1,x2],[y1,y2], linestyle=graph.get('trendLineStyle','dashed'))
                ax[count].set_yticks(np.arange(minimum,maximum+gap+1,gap))
                ax[count].set_xticks(np.arange(minimum,maximum+gap+1,gap))
                ax[count].scatter(fh,sh, marker=graph.get("scatterMarker",'.'))
                ax[count].plot(a,a)
                ax[count].set_title(col)
            count = count+1
            fig.text(0.5, 0.03, graph.get('xtitle','First Half Sub-Series'), ha='center', fontsize=graph.get('fontsize',row*colm))
            fig.text(0.01, 0.5, graph.get('ytitle','Second Half Sub-Series'), va='center', rotation='vertical', fontsize=graph.get('fontsize',row*colm))
        
        while count < row * colm:
            fig.delaxes(ax[count//colm,count%colm])
            count += 1
        plt.tight_layout(pad=5,h_pad=0.5, w_pad=1)
        plt.savefig(graph.get('output_dir','./')+name+'.png',dpi=graph.get('dpi',300))




def ITA_multiple_vis_by_column(length, graph={}, filename=[], column=[], exceptcolumn=[], csv = False, directory_path = "./"):
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
    
    row = graph.get('row', floor(len(filename)**0.5))
    colm = graph.get('colm', ceil(len(filename)/row))

    for col in column:
        fig,ax=plt.subplots(row, colm, figsize=graph.get('figsize',(colm*7,row*5)))
        count=0
        name = col

        for file in filename:
            if csv:
                x = list(pd.read_csv(directory_path+file)[col])
                ttle = file[:-4]

            else:
                x = list(pd.read_excel(directory_path+file)[col])
                ttle = file[:-5]

            x, length = preprocessing(x,length)
            fh,sh=np.array(x[:length//2]),np.array(x[length//2:])
            fh.sort()
            sh.sort()
            # print(fh,sh)
            maximum=max(max(fh),max(sh))
            minimum=min(min(fh),min(sh))
            gap = (maximum - minimum)/4
            maximum = (maximum//gap)*gap+gap
            minimum = ((minimum//gap)*gap)
            a=[minimum,maximum]
            m=np.mean(fh)
            M=np.mean(sh)
            if m>M:
                y1=minimum
                x1=minimum+m-M
                x2=maximum
                y2=maximum-m+M
            else:
                y1=minimum+M-m
                x1=minimum
                y2=maximum
                x2=maximum-M+m
            if row > 1:
                ax[count//colm,count%colm].plot([x1,x2],[y1,y2], linestyle=graph.get('trendLineStyle','dashed'))
                ax[count//colm,count%colm].set_yticks(np.arange(minimum,maximum+gap+1,gap))
                ax[count//colm,count%colm].set_xticks(np.arange(minimum,maximum+gap+1,gap))
                ax[count//colm,count%colm].scatter(fh,sh, marker=graph.get("scatterMarker",'.'))
                ax[count//colm][count%colm].plot(a,a)
                ax[count//colm][count%colm].set_title(ttle)
                

            else:
                ax[count].plot([x1,x2],[y1,y2], linestyle=graph.get('trendLineStyle','dashed'))
                ax[count].set_yticks(np.arange(minimum,maximum+gap+1,gap))
                ax[count].set_xticks(np.arange(minimum,maximum+gap+1,gap))
                ax[count].scatter(fh,sh, marker=graph.get("scatterMarker",'.'))
                ax[count].plot(a,a)
                ax[count].set_title(ttle)
            count = count+1
            fig.text(0.5, 0.03, graph.get('xtitle','First Half Sub-Series'), ha='center', fontsize=graph.get('fontsize',row*colm))
            fig.text(0.01, 0.5, graph.get('ytitle','Second Half Sub-Series'), va='center', rotation='vertical', fontsize=graph.get('fontsize',row*colm))
        
        while count < row * colm:
            fig.delaxes(ax[count//colm,count%colm])
            count += 1
        plt.tight_layout(pad=5,h_pad=0.5, w_pad=1)
        plt.savefig(graph.get('output_dir','./')+str(name)+'.png',dpi=graph.get('dpi',300))