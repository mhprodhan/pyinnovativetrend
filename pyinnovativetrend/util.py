import numpy as np
from scipy.stats import norm
import warnings
from math import isnan

def preprocessing(x, length):
    
    if length % 2 == 1:
        warnings.warn("Data series must be of even length. Earliest data will be omitted")
        length -= 1
        
    start = len(x)-length
    
    if start < 0:
        raise Exception(f"Data series is of short length, {len(x)}")
    
    for i in x:
        
        if isnan(i):
            raise Exception("Every entry must be a number")
        
    return np.array(x[start:]), length

def cor(X,Y):
    
    if len(X)==len(Y):
        Sum_xy = np.sum((X-np.mean(X))*(Y-np.mean(Y)))
        Sum_x_squared = np.sum((X-np.mean(X))**2)
        Sum_y_squared = np.sum((Y-np.mean(Y))**2)       
        corr = Sum_xy / np.sqrt(Sum_x_squared * Sum_y_squared)
    
    else:
        raise Exception (f"Sorry X (length = {len(X)}) and Y (length = {len(Y)}) must be of same length")
    
    return corr


def z2p(z_score, alpha):
    p = 2 * (1 - norm.cdf(abs(z_score)))
    h = p < alpha
    
    if h and z_score < 0:
        trend = 'Decreasing'
        
    elif h and z_score > 0:
        trend = 'Increasing'
        
    else:
        trend = 'No trend'
    
    return p, h, trend

def p2z(p_value):
    return norm.ppf(1 - p_value/2)
