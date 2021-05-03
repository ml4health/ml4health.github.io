#!/bin/bash
#
# Given an input folder of *.jpg files, 
# Produces an output folder of *.jpg files that are cropped square
#
# Usage
# -----
# $ bash create_folder_of_square_crops.sh inputdir/ outputdir/ 200

inputdir=$1
outputdir=$2

if [[ -z $3 ]]; then
    S=200
else
    S=$3
fi

for jpg_input_fpath in `ls $inputdir/*.jpg`
do
    jpg_output_fpath=`python -c "print('$jpg_input_fpath'.replace('$inputdir', '$outputdir'))"`

    echo "$jpg_input_fpath -> $jpg_output_fpath"

    convert \
        -define jpeg:size="$S"x"$S" -thumbnail "$S"x"$S"^ \
        -gravity center -extent "$S"x"$S" \
        $jpg_input_fpath $jpg_output_fpath 

done


# THIS DIDNT WORK
# convert $1 -gravity center -crop "$S"x"$S"+0+0 +repage headshots_cropped/$1


