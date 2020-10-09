#!/usr/bin/python3

import argparse
import os

# Author: n0nuser
# Description: Downloads Stream Video with ".m3u8" file and transcodes it to mp4
# Requirements: VLC installed

def args():
    desc = ("USAGE: python3 downloadStream.py -o outputFilename -i linkTo_m3u8_stream\nEg.: python3 downloadStream.py -i https://mywebsite.ext/myfile.m3u8 -o myfile")
    parser = argparse.ArgumentParser(description=desc,formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-i", type=str, help="Link of the .m3u8", dest="input", required=True)
    parser.add_argument("-o", type=str, help="Output Filename for the .mp4", dest="output", required=True)
    args = parser.parse_args()
    inp = args.input
    out = args.output
    if inp is None or out is None:
        print(desc)
        exit()
    if not inp.endswith(".m3u8",5):
        print("Input file is not .m3u8!!")
        exit()
    return out,inp

filename,streamlink = args()

os.system("vlc -I dummy --sout '#transcode{vcodec=\"avc1\",acodec=\"mp4a\"}:standard{mux=\"mp4\",dst=\"" + filename + "\",access=file}'" + streamlink)
