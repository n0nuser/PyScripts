#!/usr/bin/python3
import argparse
import os
import subprocess

def args():
    desc = "Convert webm to mp3."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-i", help="Name of Input File", type=str, dest="input")
    parser.add_argument("-o", help="Name of Output File", type=str, dest="output")
    inp = str(parser.parse_args().input)
    out = str(parser.parse_args().output)
    if inp is None or out is None:
        print("usage: webm2mp4.py [-h] [-i INPUT] [-o OUTPUT]")
        exit()
    if not out.endswith(".mp3",4):
        print("Output file is not .mp3!!")
        exit()
    return inp,out


inp, out = args()

# Verifies ffmpeg is installed
status, result = subprocess.getstatusoutput("which ffmpeg")
if status == 1:
    print("ffmpeg needed!\nTo install it: sudo apt install ffmpeg -y")

cmd_string = 'ffmpeg -i "' + inp + '" -vn -ab 128k -ar 44100 -y "' + out + '"'
print('converting ' + inp + ' to ' + out)
os.system(cmd_string)
