import time
import asyncio

async def async_find_divisibles(in_range, divisor):
    start_time = time.time()
    divisibles=[]
    print(f"\nasync_find_divisibles called with range {in_range} and divisor {divisor}.")
    
    for i in range(1, in_range):
        if i%divisor==0: 
            divisibles.append(i)
            await asyncio.sleep(0)
            
    end_time = time.time()
    print(f"async_find_divisibles ended with range {in_range} and divisor {divisor}. It took {1000*(end_time-start_time)} miliseconds\n")
    return divisibles

async def main():
    # create three asynchronous tasks
    task1 = asyncio.create_task(async_find_divisibles(50800000, 34113))
    task2 = asyncio.create_task(async_find_divisibles(100052, 3210))
    task3 = asyncio.create_task(async_find_divisibles(500, 3))
    
    results1 = await task1
    results2 = await task2
    results3 = await task3
    
    print("list 2: ", results2, "\n")
    print("list 3:", results3, "\n")

if __name__ == "__main__":
    asyncio.run(main())
