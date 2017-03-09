Stitching
=========

Stitch images to form a montage.

Requirements
============

Java development kit

Python 2.7.12

pip

numpy
  $ pip install numpy

scipy
  $ pip install scipy

click
  $ pip install click

skimage
  $ pip install skimage

python-bioformats
  $ pip install python-bioformats

matplotlib
  $ pip install matplotlib

Additional in Windows OS: Visual C++ 9.0

Installation
============

  $ git clone https://github.com/CellProfiler/stitching.git

  $ cd /path/to/stitching

  $ pip install -e .

Info
====
Users may notice that when opening and zooming the images in IDEAS (and also in ImageJ, IrfanView) the images appear to be higher resolution, but this is because the software has an adjustable DPI setting, which uses interpolation to scale the images up (adding pixels) for display and publication.

Use
===

  $ python stitching -o path/to/OUTPUT_DIRECTORY path/to/IMAGE

Generates per-channel tiled images from IMAGE saved to OUTPUT_DIRECTORY. Each image in IMAGE has shape 55px by 55px and
is padded with random noise. Files are named "ch1.tif", "ch2.tif", ..., one for each channel.

cif-reader
============
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
