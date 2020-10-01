#!/usr/bin/python3
import argparse
import os
import subprocess

# ffmpeg needed

def args():
    desc = "Convert webm to mp4."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-i", help="Name of Input File", type=str, dest="input")
    parser.add_argument("-o", help="Name of Output File", type=str, dest="output")
    inp = parser.parse_args().input
    out = parser.parse_args().output
    if inp is None or out is None:
        print("usage: webm2mp4.py [-h] [-i INPUT] [-o OUTPUT]!")
        exit()
    return inp,out


inp, out = args()

status, result = subprocess.getstatusoutput("which ffmpeg")
if status == 1:
    print("ffmpeg needed!\nTo install it: sudo apt install ffmpeg -y")

mp4_file = inp.replace('.webm','.mp4')
cmd_string = 'ffmpeg -i "' + inp + '" "' + mp4_file + '"'
print('converting ' + inp + ' to ' + mp4_file)
os.system(cmd_string)