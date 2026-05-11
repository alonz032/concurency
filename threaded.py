#include <iostream>
#include <thread>
#include <chrono>

void count_big(int id) {
    long long count = 0; 
    for (long long i = 0; i < 100000000; ++i) {
        count += 1; 
    }
    std::cout << "Thread " << id << " finished.\n";
}

int main() {
    // START CLOCK
    auto start = std::chrono::high_resolution_clock::now();

    // Launch 3 threads on 3 separate cores
    std::thread t1(count_big, 1);
    std::thread t2(count_big, 2);
    std::thread t3(count_big, 3);

    t1.join();
    t2.join();
    t3.join();

    // END CLOCK
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> diff = end - start;

    std::cout << "\nTOTAL C++ TIME: " << diff.count() << "s" << std::endl;

    return 0;
}