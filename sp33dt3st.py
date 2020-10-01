#!/usr/bin/python3
import speedtest
import argparse
import os

def name():
    desc = "Speedtest"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-m", help="Name of Output File", type=str, dest="name")
    name = parser.parse_args().name
    return name

name = name()

interface = '''\033[1;95m
    _____                     ________          __ 
   / ___/____  ___  ___  ____/ /_  __/__  _____/ /_
   \__ \/ __ \/ _ \/ _ \/ __  / / / / _ \/ ___/ __/
  ___/ / /_/ /  __/  __/ /_/ / / / /  __(__  ) /_  
 /____/ .___/\___/\___/\__,_/ /_/  \___/____/\__/  
     /_/                                           
\033[0m
'''
print(interface)
print(" Por favor, espere \033[5m...\033[0m")
st = speedtest.Speedtest()
st.get_best_server()
download = round(float(st.download())/1000000,4)
upload = round(float(st.upload())/1000000,4)


# Formats and prints
d = "\033[1;96m Bajada\033[0m: " + str(download) + " (mb/s)"
u = "\033[1;96m Subida\033[0m: " + str(upload) + " (mb/s)"
os.system("clear")
print(interface)
print(d)
print(u)

# Saves to file
f = open(name,"w")
f.write(d + "\n" + u)
f.close()
