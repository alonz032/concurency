import threading
import time

def count_to_100m(id):
    print(f"[Thread {id}] Starting CPU work...")
    count = 0
    for i in range(100_000_000):
        count += 1
    print(f"[Thread {id}] Finished.")

if __name__ == "__main__":
    start_time = time.time()

    # Launching 3 "Threads"
    t1 = threading.Thread(target=count_to_100m, args=(1,))
    t2 = threading.Thread(target=count_to_100m, args=(2,))
    t3 = threading.Thread(target=count_to_100m, args=(3,))

    t1.start(); t2.start(); t3.start()
    t1.join(); t2.join(); t3.join()

    print(f"\nTOTAL THREADING TIME: {time.time() - start_time:.2f}s")