# SubtitleConverter
Converts VTT subtitle to SRT subtitle and vice versa.

#How to use
Issue the following command on your terminal:

    # chmod u+x subtitle-Converter.py
    # ./subtitle-Converter.py -i <input vtt file> -o <output srt file> -s
    
OR

    # chmod u+x subtitle-Converter.py
    # ./subtitle-Converter.py -i <input srt file> -o <output vtt file> -d
    
Volia! Done!

#Help! I need to convert to VTT or SRT file recursively in my directory!
Run `recursivelyConvertSubtitle.sh` on your terminal (**By default it convert from vtt to srt**)! Use the following if you want to convert SRT file to VTT file:

    #!/bin/bash
    
    OIFS=$IFS
    IFS=$'\n'
    
    for file in `find . -iname *.vtt -type f`; do
      filename=$(basename $file)
      xbase=${file##*/}
      fileprefix=${xbase%.*}
      xpath=$(dirname $file)
      
      outputPath="$xpath/$fileprefix.vtt" # Edit the extension accordingly
      echo $outputPath
      ./subtitle-Converter.py -i $file -o $outputPath -d
    done
