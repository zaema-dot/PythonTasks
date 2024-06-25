import argparse
import json
import random
import math

def monte_carlo(its):
    points_in_circle = 0 # define the number of points that lie inside the circle
    total_points = 0
    
    # define a for loop that generates rando coordinates(x,y) in the range (-1,1)
    for i in range(its):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        total_points+=1
                
        # check if random point lies inside the circle
        if x**2 + y**2 <=1:
            points_in_circle +=1
            
    # area of circle over area of square
    # 1 side of square = 2r, area = (2r)2 so = 4r^2
    # radius of circle = r, area = pi*r^2
    # P(points_in_circle)=pi/4
    # pi = 4*P(points in circle)
    # pi ~ 4* points_in_circle/total_points
    return(points_in_circle/total_points)*4

def main():
    # create an argparse object to process the command line arguments
    parser = argparse.ArgumentParser(description = "monte carlo for pi estimation", usage="Monte Carlo simulation for estimating the value of π.\nUsage examples:\npython task4.py -i 100000\npython task4.py -j") 
    # add the argument for the -i flag that defines the number of iterations
    parser.add_argument('-i', type = int, help ="number of iterations")
    # add the argument for the -j flag that takes the number of iterations from iterations.json
    parser.add_argument('-j', action = 'store_true', help = "read the json file")

    args = parser.parse_args()
    
    if args.j: #if the command line flag is j then read the json file 
        try:
            with open('iterations.json','r') as file:
                content = json.load(file)
                its = content['iterations']
        except FileNotFoundError: # error exception if the file doesn't exist
            print("Error: iterations.json file not found.")
        except KeyError:
            print("the key does not exist")
            return
    elif args.i: # if the command line flag is i then set the number of iterations to that input
        its = args.i
    else:
        parser.print_help()
        return
    
    pi = monte_carlo(its) # estimate the value of pi and print it
    print(f"estimated value of pi after {its} iterations = {pi}")
        
    
if __name__ == "__main__":
    main()

        
                
                