#!/usr/bin/python
#filename lc_base.py

"""
file name lc_base
lightcurve functions to help with our basic analysis and use in our
interactive examination of the synthetic light curves for student learning
about basic light curves. I will include more info here as I develop them.

Version history:
July 13, 2016  finished main version
July 18, 2016  some name changes
July 21, 2016  some name changes, added error coding and comments
"""

def set_path():
    """ 
    queries user for directory and then checks to make sure it is valid
    it also adds the final / if left off so that the path could be combined
    with a filename, generally used in intractive session
        inputs:         no function input, but queries user
        outputs:  
            path        string with path 
        
        example call:
        path1=lc_base.set_path()
    """
    
    # import os so we can check path validity 
    import os
    
    # to keep backwards compatibility on python2 and python3
    from six.moves import input
    
    # query user for file name 
    path = input("Enter the light curve directory: ")

    
    # check if it is a valid directory
    #   if it is valid, and does not end with /, fix that
    #   print the path and return that value
    # if directory was not valid, report and don't return a value
    if os.path.isdir(path):
        if not (path.endswith('/')): 
            path=path+'/'
        print("setting light curve directory to: "+path)
        return path
    else:
        print("directory was not valid")
        return None

#-------------------------------------------------------------------------     
    
    
def set_file():
    """ 
    queries user for a filename, used in interactive mode
    input:              none
    output:
        filename        a string with the filename
    """
    # to keep backwards compatibility on python2 and python3
    from six.moves import input
    
    # query user for file name
    filename = input("Enter a filename: ")


    return filename

#------------------------------------------------------------------------- 
    
    
def read_ascii_cols(filename,tcol=0,fcol=1):
    """
    Read in a light curve from an ascii file and return the data for time and
    brightness as two arrays. It can work for both space and comma separated
    
    input:
        filename        string with full path and filename
    optional input:
        tcol            integer with column number for time (starts at 0)
        fcol            integer with column number for flux
    output:
        time            numpy array of time values
        flux            numpy array of flux values
    
    """
    import numpy as np
    from astropy.io import ascii

    # read in the data from the file, it goes into a table format
    try:    
        data = ascii.read(filename)
    except:
        print("Error reading file "+filename)
        return None


    # convert the table into numpy arrays
    time = np.array(data.columns[tcol])
    flux = np.array(data.columns[fcol])
    
    # return the arrays
    return time, flux


#------------------------------------------------------------------------- 
    
def lc_plot(time,flux,title='lc',ms=2,**kwargs):
    """
    This creates the plot from two arrays    
    """
    import matplotlib.pyplot as plt
    
    plt.figure(title)
    plt.plot(time, flux, '.', ms=ms,**kwargs)
    plt.xlabel('time')
    plt.ylabel('flux')
    plt.show()
    
    return 

#------------------------------------------------------------------------- 


def quick(filename, path='foo',tcol=0,fcol=1):
    """
    For a quick readin and look at ascii based light curve files
    input:
        filename        a string containing the filename (optionally with path)
    optional input:
        path            a string containing the path to the file
        tcol            the column for the time data
        fcol            the column for the flux data
    output:
        time            numpy array of time values
        flux            numpy array of flux values
    """
    import os

    #check to see if the file is a full path file, if yes then move forward
    if (os.path.isfile(filename)): fullname=filename
    elif (os.path.isfile(path+filename)): fullname =path+filename
    # if given directory is not valid, then ask for full file
    else:
        print("file was not valid")
        filename=set_file()
        if (os.path.isfile(filename)): fullname=filename
        elif (os.path.isfile(path+filename)): fullname =path+filename
        else: 
            print("file still not valid")
            return None, None
    
    time,flux=read_ascii_cols(fullname,tcol,fcol)
    
    lc_plot(time,flux,filename)
    
    return time,flux
    
        
#------------------------------------------------------------------------- 


    

    
    
""" example for how to use some of these    
path=set_path()
filename=set_file()
time,flux=quick(filename,path)

lc_plot(t2,f2,'syndata')
newfile=set_file()


"""