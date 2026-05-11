import time

def count_big(counter_id):
    print(f"Count #{counter_id} starting...")
    count = 0
    # Counting to 100 Million
    for i in range(100_000_000):
        count += 1
    print(f"Count #{counter_id} finished. Result: {count}")

if __name__ == "__main__":
    start_time = time.perf_counter()

    # Running 3 times consecutively
    count_big(1)
    count_big(2)
    count_big(3)

    end_time = time.perf_counter()
    print(f"\nTOTAL PYTHON CONSECUTIVE TIME: {end_time - start_time:.4f}s")