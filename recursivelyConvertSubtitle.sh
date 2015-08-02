#!/bin/bash

OIFS=$IFS
IFS=$'\n'

for file in `find . -iname *.vtt -type f`; do
    filename=$(basename $file)
    xbase=${file##*/}
    fileprefix=${xbase%.*}
    xpath=$(dirname $file)
    
    outputPath="$xpath/$fileprefix.srt" # Edit the extension accordingly
    echo $outputPath
    ./subtitle-Converter.py -i $file -o $outputPath -s # For VTT to SRT, change -s to -d for SRT to VTT
done
