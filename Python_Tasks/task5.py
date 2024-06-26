from math import *
import matplotlib.pyplot as plt

def square(l1):
    #return the square of all elements in the list
    return [x ** 2 for x in l1]

        
def cube(l1):
    #return the cube of all elements in the list
    return [x ** 3 for x in l1]

def plot_graph(x, sq, cu):
    #plot square graph 
    # set the figure dimensions
    plt.figure(figsize =(10, 5))
    # create two subplots, this one's the first plot
    # plt.subplot(1,2,1)
    # plot data points
    plt.plot(x, sq)
    plt.plot(x,cu)
    plt.title('Square of Numbers')
    plt.xlabel('Number')
    plt.ylabel('Square')
    plt.grid(True)
    
    # # Plot cube
    # plt.subplot(1, 2, 2)
    # plt.plot(x, cu)
    # plt.title('Cube of Numbers')
    # plt.xlabel('Number')
    # plt.ylabel('Cube')
    # plt.grid(True)

    # Show the plots
    plt.tight_layout() # make sure plots fit in the figure area.
    plt.show()

def main():
    # define a list with the first 10 natural numbers
    x = [1,2,3,4,5,6,7,8,9,10]
    # get the square of the list
    sq = square(x)
    # get the cube of the list
    cu = cube(x)

    plot_graph(x,sq,cu)
    
    

if __name__ == "__main__":
    
    main()