#!/bin/bash

input_filename=$1
output_filename=`python -c "import os; print os.path.splitext('$input_filename')[0] + '_500x200.png'"`

echo "IN : $input_filename"
echo "OUT: $output_filename"

convert $input_filename \
     -resize 500x200 -gravity center -extent 500x200 \
     $output_filename
