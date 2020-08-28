#!/bin/bash
#
# Usage
# -----
# $ bash convert_png_to_jpg.sh myfilepath.png

infile=$1
outfile=`python -c "print ('$1'.replace('.png', '.jpg'))"`

convert $infile $outfile


