#!/usr/bin/python

import sys
import argparse
import os
import re

def argumentCheck():
    parser = argparse.ArgumentParser(description='Converts subtitle from VTT to SRT or vice versa')
    parser.add_argument('--input', '-i', type=argparse.FileType('r'), help='Input file')
    parser.add_argument('--output', '-o', type=argparse.FileType('w'), default=sys.stdout, help="Output file")
    parser.add_argument('--toSrt', '-s', action='store_true', help='Convert VTT to SRT')
    parser.add_argument('--toVtt', '-d', action='store_true', help='Convert SRT to VTT')
    
    args = parser.parse_args()
    if len(sys.argv) == 1 or args.toSrt == args.toVtt:
        parser.print_help()
        sys.exit(1)

    return args

def srtToVtt(lines, srtPattern):
    counter = 0
    lines.insert(0, "")
    lines.insert(0, "WEBVTT")
    for line in lines:
        if re.match(srtPattern, line):
            line = re.sub(r",", ".", line)

        lines[counter] = line.strip()
        counter += 1

    return lines

def vttToSrt(lines, vttPattern):
    START_FROM_LINE = 2
    counter = 0

    lines = lines[START_FROM_LINE:]
    for line in lines:
        if re.match(vttPattern, line):
            line = re.sub(r"\.", ",", line)

        lines[counter] = line.strip()
        counter += 1

    return lines

def main():
    args = argumentCheck()

    vttTimePattern = "(\d){2,}:(\d){2,}:(\d){2,}\.(\d){3}"
    srtTimePattern = "(\d){2,}:(\d){2,}:(\d){2,},(\d){3}"
    vttPattern = " --> ".join([vttTimePattern, vttTimePattern])
    srtPattern = " --> ".join([srtTimePattern, srtTimePattern])

    if not args.input == None:
        lines = args.input.readlines()
        if args.toSrt:
            outputLines = vttToSrt(lines, vttPattern)
        elif args.toVtt:
            outputLines = srtToVtt(lines, srtPattern)

    with args.output as file_:
        for line in outputLines:
            file_.write(line)
            file_.write("\n")

main()