# -*- coding: utf-8 -*-
from astropy.io import ascii
import os
"""
syn.py
This is a collection of synthetic light curve tools.
This uses the python 3 syntax for input

Created on Wed Jul 20 10:49:45 2016
@author: jcash
"""

def make_basic(period=10.0,noise_sigma=0,amp=1.0):
    ''' Create synthetic lightcurve file
        for now most of the stuff will be hardcoded and then added as options
    optional input:
        period          value for period, int or float, default is 10
        noise_sigma     sigma value for normal distribution
                            if noise_sigma is not >0 then no noise
        amp             value for amplitude, default is 1.0
    output:
        time    nparray of time values
        flux    nparray of flux values        
        
    last modified:  JLC 2016/07/20
    '''
    import numpy as np
    
    # input values can be passed as parameters or will default to values
    # generally the period will be passed and the noise_sigma may be passed    
    
    #set the length of the data set (number of data points)
    tlength= 1000    
    
    #set the initial time data point
    tstart = 0.0
    
    #set the time span of the data set (start to end time)
    tspan = 500

    # create the array as evenly spaced (assume no gaps right now)    
    time=np.linspace(tstart,(tstart+tspan),tlength)

    
    # convert period to float if it was integer
    period=float(period)
    
    
    # calculate the noise array (normal distribution)
    if (noise_sigma>0):
        noise=np.random.normal(0,noise_sigma,tlength)
    else:
        noise=np.zeros(tlength)
    
    
    # create the flux array to match the time array
    flux= amp*np.sin((2*np.pi/period*time))+noise
    
    return time, flux
   
def make_gaps(time,flux,fraction=0.5):
    ''' Create random gaps in a synthetic lightcurve 
    optional input:
        time          nparray of time values
        flux          nparray of flux values
        fraction        fraction of points excluded
    output:
        tok     nparray of time values left after removing points
        fok     nparray of flux values left after removing points
        
    last modified:  JLC 2016/10/04
    '''

    import numpy as np
    
    # input values can be passed as parameters or will default to values
    # generally the period will be passed and the noise_sigma may be passed    
    
    #set the length of the data set (number of data points)
    tlength= time.size    

   
    #create a random array for creating gaps
    gaps=np.random.rand(tlength)   
    tok=time[gaps>=fraction]    
    fok=flux[gaps>=fraction]
    
    
    return tok,fok
    
  
    
def write(time, flux, filename):
    """
    write out a synthetic light curve to an ascii file
    inputs:
        time        an array of time values
        flux        an array of flux values
        filename    a filename including path
    output:
        none
    actions:
        the new file is created

    last modified:  JLC 2016/07/20
    """
    # checks that the data is okay, two array of same length
    len1 = len(time)
    len2 = len(flux)
    if len1 != len2:
        print('Error: arrays are not the same length')
        return

    #check to see if the file already exists, ask if you want to clobber
    if os.path.isfile(filename):
        print(filename+' already exists. ')
        tmp1 = input('Overwrite this file? (y/n) ')
        if tmp1 == 'y':
            pass
        else:
            return

    # write data out to the file
    ascii.write([time, flux], filename)


def multi(vals,noise=0):
    """       
    A quick program to create a multiperiodic synthetic lightcurve.
    Right now it is quite picky about the format for the vals input.
    Ideally the vals should be a list of [period,amp] pairs.
    If you don't care about the amplitude, you can give a list of periods,
    but they still need to be inside a list of lists [[p1],[p2],[p3]]
    
    input:
        vals            a list of lists with period and amp
    optional input:     
        noise               the noise_sigma value
    outputs:
        time            an array of time values
        flux            an array of flux values
    
    last modified: JLC 2016/07/20

    """     
    #check the length of vals, 
    if len(vals)<2:
        print('multiple values not given')
        return None
     
    #use the first item in list as first period or period.amp pair
    
    if len(vals[0])==1:
        time,flux=make_basic(vals[0],noise)
    elif len(vals[0])==2:
        time,flux=make_basic(vals[0][0],noise,amp=vals[0][1])
    else:
        print('first value is not a single or pair')
        return None
    
    #now for remaining ones in the list
    for item in vals[1:]:
        if len(item)==1:
            t,f=make_basic(item[0])
            flux=flux+f
        elif len(item)==2:
            t,f=make_basic(item[0],amp=item[1])
            flux=flux+f
        else: 
            ('the values '+item+' are not single or pair')
        
    return time,flux
    


    
"""
## Examples for how to run some of these codes
from lightcurves import syn

#to make a singly periodic lightcurve
time,flux=syn.make_basic(period,noise,amplitude)
time,flux=syn.make_basic(10.0,0.05,1.0)


#to make a multiperiodic lightcurve
#define values for each period and amplitude
vals=[[10.2,0.3][14.2,0.2],[56.2,0.6]]
time,flux=syn.multi(vals,noise)

# to write out the new synthetic lightcurve
filename='somepath/file'
syn_write(time,flux,filename)
"""
