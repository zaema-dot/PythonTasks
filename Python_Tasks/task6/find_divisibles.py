from datetime import datetime, time
import time


def find_divisibles(in_range, divisor):
    divisibles=[]
    print(f"\nfind_divisibles called with range {in_range} and divisor {divisor}.")
    start_time = time.time()
    for i in range(1, in_range):
        if i%divisor==0:
            divisibles.append(i)
    end_time = time.time()
    print(f"find_divisibles ended with range {in_range} and divisor {divisor}. It took {1000*(end_time-start_time)} miliseconds\n")
    return divisibles

def main():
    l1 = find_divisibles(50800000, 34113)
    l2 = find_divisibles(100052, 3210)
    l3 = find_divisibles(500, 3)
    
    print("list 2: ", l2, "\n")
    print("list 3: ", l3, "\n")
    
if __name__ == "__main__":
    main()
            
        