#!/bin/bash

if [[ -z $2 ]]; then
    S=500
else
    S=$2
fi

convert -define jpeg:size="$S"x"$S" $1 -thumbnail "$S"x"$S"^ \
          -gravity center -extent "$S"x"$S" "../headshots_""$S"x"$S/$1"

# THIS DIDNT WORK
# convert $1 -gravity center -crop "$S"x"$S"+0+0 +repage headshots_cropped/$1


