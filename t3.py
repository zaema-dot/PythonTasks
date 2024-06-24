# Task # 3
# Suppose you are a hardware enthusiast and love checking the system’s details. 
# To make your task easy you have to write a program that is used to check the hardware details of a system 
# and generates a file for you; named “Specs.txt '' at a location “/home/Username/Details”. 
# If the directory “Details'' does not exist on your system you have to create it. 
# Details you are interested in are given below along with example values. 
# Remember you are not allowed to code in iPython. You can only use the Python3 interpreter. 
# Username will be the name of the user on your system for example “/home/<username>/Details''

# Byte Order:          Little Endian
# Core(s) per socket:  4
# Socket(s):           1
# Model name:          Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz
# CPU MHz:             1638.462
# CPU max MHz:         4000.0000
# CPU min MHz:         400.0000
# Virtualization Support:      VT-x
# L1           32K
# L2 cache:            256K
# L3 cache:            8192K
# RAM Memory: 15794MB

# Note: You have to find a way to show only the hardware details mentioned above.

import psutil
import platform
from datetime import datetime
import sys
import os
import subprocess
import re

cpu_sockets =  int(subprocess.check_output('cat /proc/cpuinfo | grep "physical id" | sort -u | wc -l', shell=True))
print("number of sockets: ",cpu_sockets)

print(sys.byteorder, 'Endian')
print("Core(s) per socket': " , psutil.cpu_count(logical=False))

def get_processor_name():
    try:
        result = subprocess.run(['lscpu'], capture_output=True, text=True, check=True)
        lines = result.stdout.splitlines()
        for line in lines:
            if "Model name" in line:
                # Split the line at the colon and strip any leading/trailing whitespace from the second part
                return line.split(':', 1)[1].strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "Unknown"

print("Model Name: ", get_processor_name())


def get_frequencies():
    freqs = psutil.cpu_freq()
    
    print("CPU MHZ: ", freqs[0])
    print("CPU min MHZ: ", freqs[1])
    print("CPU max MHZ: ", freqs[2])
    return()

    
get_frequencies()


def get_virtualization_support():
    """
    Retrieves virtualization support information using lscpu command.
    """
    try:
        result = subprocess.run(['lscpu'], capture_output=True, text=True, check=True)
        lines = result.stdout.splitlines()
        for line in lines:
            if 'Virtualization' in line:
                return line.split(':')[1].strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "Unknown"
    
print(get_virtualization_support())