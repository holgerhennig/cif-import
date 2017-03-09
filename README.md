# cif-reader
This module reads image data from compensated image files (.cif files) into a tensor in python.

Requirements
============
bioformats
   $ pip install bioformats
javabridge
   $ pip install javabridge
numpy
   $ pip install numpy
math
   $ pip install math

Use
============
Imaging flow cytometry (IFC) instruments by Millipore generate cif files, which contain images and metadata. This module reads image data from cif files into a tensor in python. Optionally the images are padded and cropped such that they have the same dimensions. The image data in the tensor can then readily be fed, e.g., into deep learning networks such as convolutional neural netowrks.

#import the ifc module
import ifc
filelist = ['blasts.cif', 'normal.cif']
T = ifc.read_cif(filelist)
