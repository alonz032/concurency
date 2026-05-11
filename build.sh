import multiprocessing
import time

def count_to_100m(id):
    print(f"Worker {id} started counting...")
    count = 0
    # True CPU work - no simulation with "sleep"
    for i in range(100_000_000):
        count += 1
    print(f"Worker {id} finished.")
    return count

if __name__ == "__main__":
    # --- SETUP ---
    start_time = time.time()
    
    # --- PARALLELISM Attempt ---
    # We create 3 separate Processes. 
    # Each one may get its own CPU Core.
    p1 = multiprocessing.Process(target=count_to_100m, args=(1,))
    p2 = multiprocessing.Process(target=count_to_100m, args=(2,))
    p3 = multiprocessing.Process(target=count_to_100m, args=(3,))

    # They all start at the EXACT same time
    p1.start()
    p2.start()
    p3.start()

    # Wait for all of them to finish
    p1.join()
    p2.join()
    p3.join()

    end_time = time.time()
    print(f"\nTOTAL TIME: {end_time - start_time:.2f}s")