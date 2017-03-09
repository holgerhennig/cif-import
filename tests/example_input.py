#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 15:28:53 2017
@author: holgerh
"""


# TODO: can javabridge.start_vm be added to module ifc.py?
import bioformats
import javabridge
javabridge.start_vm(class_path=bioformats.JARS, max_heap_size='8G')

# path to directory with input .cif files
import os
os.chdir('/Users/holgerh/Dropbox/holger/work/Academia/projects/DeepLearning/ifc_module')
import ifc

filelist = ['blasts.cif', 'normal.cif']

# optional input parameters
# classes = ['normal', 'blast'] # [optional] classes name strings need to be filename strings for automatically assigning labels. default is no classes provided (classes=0)
# channels = [0,5] # [optional] default is all 12 channels 0-11 # channels = [0,5,6,11]
# pad=1 # [optional] padding or cropping of images, default is no padding (pad=0)
# verbose=1 
    
T = ifc.read_cif(filelist) #minimal version
#T, L = ifc.read_cif(filelist, channels=channels, classes=classes, pad=pad, verbose=verbose) #with all optional parameters

