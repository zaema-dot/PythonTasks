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
    print("here")
    parser = argparse.ArgumentParser(description = "monte carlo for pi estimation", usage="Monte Carlo simulation for estimating the value of π.\nUsage examples:\npython Main.py -i 100000\npython Main.py -j") 
    parser.add_argument('-i', type = int, help ="number of iterations")
    parser.add_argument('-j', action = 'store_true', help = "read the json file")

    args = parser.parse_args()
    
    if args.j:
        try:
            with open('iterations.json','r') as file:
                content = json.load(file)
                its = content['iterations']
        except FileNotFoundError:
            print("Error: Iterations.json file not found.")
            return
    elif args.i:
        its = args.i
    else:
        parser.print_help()
        return
    
    pi = monte_carlo(its)
    print(f"estimated value of pi after {its} iterations = {pi}")
        
    
if __name__ == "__main__":
    main()

        
                
                