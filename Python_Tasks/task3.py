"""
Task # 3
Byte Order:          Little Endian
Core(s) per socket:  4
Socket(s):           1
Model name:          Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz
CPU MHz:             1638.462
CPU max MHz:         4000.0000
CPU min MHz:         400.0000
Virtualization Support:      VT-x
L1           32K
L2 cache:            256K
L3 cache:            8192K
RAM Memory: 15794MB """

import psutil
from datetime import datetime
import sys
import subprocess
import os

# define the directory and file path
username = os.getlogin()  # get the current user's username
directory = f"/home/{username}/Details"
file_path = os.path.join(directory, "Specs.txt")

# ensure the directory exists
if not os.path.exists(directory):
    os.makedirs(directory)

def num_of_sockets():
    # get the number of sockets
    
    # Execute the command and capture the output
    cpu_sockets = subprocess.check_output("lscpu | grep 'Socket(s):' | awk '{print $2}'", shell=True, text=True)
    
    # Convert to integer and print the number of sockets
    print("number of sockets: ", int(cpu_sockets))     
    return f"Number of sockets: {int(cpu_sockets)}"

def get_byte_order():
    # get the byte order using sys library
    print("Byte Order: " , sys.byteorder, 'Endian')
    get_cores_per_socket()    
    return f"Byte Order: {sys.byteorder} Endian"

def get_cores_per_socket():
    # get the number of cores per socket using the lscpu command with the subprocess library
    cps = subprocess.check_output("lscpu | grep 'Core(s) per socket:' | awk '{print $4}'", shell=True, text=True)
    print("Core(s) per socket: " , cps)
    return f"Core(s) per socket: {cps}"

def get_process_name():
    #get the processor name/model name
    processor_name = subprocess.check_output("lscpu | grep 'Model name' | xargs ", shell=True, text=True)
    print("Model name: ", str(processor_name))
    return f"Model name: {processor_name}"

def get_frequencies():
    # get the cpu frequency, and the min and max frequencies
    freq = subprocess.check_output("lscpu | grep 'CPU MHz:' | xargs | awk '{print $3}' ", shell=True, text=True)
    print("CPU MHZ: ", freq)
    
    maxfreq = subprocess.check_output("lscpu | grep 'CPU max MHz:' | xargs | awk '{print $4}' ", shell=True, text=True)
    print("CPU max MHZ: ", maxfreq)
    
    minfreq = subprocess.check_output("lscpu | grep 'CPU min MHz:' | xargs | awk '{print $4}' ", shell=True, text=True)
    print("CPU min MHZ: ", minfreq)
    return f"CPU MHz: {freq}\n CPU max MHz: {maxfreq}\nCPU min MHz: {minfreq}"

def get_virtualization_support():
    # get teh virtualization support     
    virt = subprocess.check_output("lscpu | grep 'Virtualization' | xargs | awk '{print $2}' ", shell=True, text=True)
    print("Virtualization: ", str(virt))
    return f"Virtualization: {virt}"
    
def get_cache_size():
    #get L!i, L2 and L3 cache sizes
    l1 = subprocess.check_output("lscpu | grep 'L1i cache:' | xargs | awk '{print $3}' ", shell=True, text=True)
    print("L1 Cache: ", str(l1))
    
    l2 = subprocess.check_output("lscpu | grep 'L2 cache:' | xargs | awk '{print $3}' ", shell=True, text=True)
    print("L1 Cache: ", str(l2))
    
    l3 = subprocess.check_output("lscpu | grep 'L3 cache:' | xargs | awk '{print $3}' ", shell=True, text=True)
    print("L3 Cache: ", str(l3))
    return f"L1 Cache: {l1}\nL2 Cache: {l2}\nL3 Cache: {l3}"

def get_RAM_Mem():
    #get the RAM Memory using psutil
    ram = psutil.virtual_memory().total
    print("RAM Memory: ", ram//(1024 **2), " MB") #convert it to MBs
    return f"RAM Memory: {ram//(1024**2)} MB"

def get_numa_node():
    node = subprocess.check_output("lscpu | grep 'NUMA node(s):' | xargs | awk '{print $3}' ", shell = True, text = True)
    print("node = ", str(node))
    return f"node = {node} \n"

def main():
    # gather and print hardware details and save the in specs.txt
    details = [ 
                get_byte_order(),
                num_of_sockets(),
                get_process_name(),
                get_frequencies(),
                get_virtualization_support(),
                get_cache_size(),
                get_RAM_Mem(),
                get_numa_node()
                ]
    
    with open(file_path, 'w') as file:
        file.write("\n".join(details)) #use join to join the outputs of the list.
        
    
if __name__ == "__main__":
    
    main()