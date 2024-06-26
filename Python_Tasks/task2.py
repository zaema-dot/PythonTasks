# Task 2: In the example below, the numbers after the directions are steps. 
# Please write a program to compute the distance from the current position after a sequence of movements and the original point.  
# If the distance is a float, then just print the nearest integer.  
# Use the argparse library to take inputs for UP, DOWN, LEFT, and RIGHT.  
# Example: If the following tuples are given as input to the program:  
# UP 5  
# DOWN 3  
# LEFT 3  
# RIGHT 2  
# Then, the output of the program should be: 2  
# Note: Handling of incorrect inputs will be appreciated along with a guide to enter the correct inputs

import argparse
import math
from math import *

# define a function to get the moves from the argument parse
def movement():
    
    # create a parser object
    parser = argparse.ArgumentParser(description="Compute distance from the original point after movements.")
    
    # add arguments
    parser.add_argument('--UP', type=float, default=0, help='Steps to move up (non-negative number)')
    parser.add_argument('--DOWN', type=float, default=0)
    parser.add_argument('--LEFT', type=float, default=0)
    parser.add_argument('--RIGHT', type=float, default=0)
    
    # parse the arguments
    args = parser.parse_args()   
    
    if args.UP < 0 or args.DOWN < 0 or args.LEFT < 0 or args.RIGHT < 0:
        parser.error("All movement values must be non-negative numbers.") 
    
    return args

# define a function to calculate resultant coordinates after adding moves
def calc_new_coord(args):
    
    # access the arguments
    net_up = args.UP
    net_down = args.DOWN
    net_left = args.LEFT
    net_right = args.RIGHT
    
    # print the values to demonstrate
    print(f"UP: {net_up}")
    print(f"DOWN: {net_down}")
    print(f"LEFT: {net_left}")
    print(f"RIGHT: {net_right}")
    
    
    # assuming starting coords are (0,0), calculate resulting coords by adding the net movements
    res_coord = ((0+net_up-net_down),(0+net_right-net_left))
    print("new coordinates: ", res_coord)
    
    return res_coord

# define a function to calculate the euclidean distance 
def calc_dist(res_coord):
    x = res_coord[0]
    y = res_coord[1]
    dist = int(sqrt((x*x)+(y*y)))
    return dist
    

def main():
        
    # get the arguments using the movement function    
    args = movement()
    
    # calculate the resultant coords using the args
    res = calc_new_coord(args)
    
    # calculate the distance using new coords
    dist = calc_dist(res)
    
    # print the distance
    print("The distance is: " + str(dist))

if __name__ == "__main__":
    
    main()
    #check if u can take another input from the command line after a wrong input.

