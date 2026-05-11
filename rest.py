#include <iostream>
#include <thread>
#include <mutex>
#include <chrono>
#include <string>
#include <vector>

using namespace std;

// --- GLOBAL RESOURCES ---
mutex stove_lock;
// TODO: Declare a mutex for the Airfryer


auto start_time = chrono::steady_clock::now();

// --- LOGGING ---
void log_event(string task, string msg) {
    auto now = chrono::steady_clock::now();
    double elapsed = chrono::duration<double>(now - start_time).count();
    
    // Note: This printf is thread-safe but not atomic. 
    // It works fine for one-line logs!
    printf("[%.2fs] [%s] %s\n", elapsed, task.c_str(), msg.c_str());
}

// --- INDEPENDENT TASKS ---

void makeTea() {
    log_event("TEA", "Starting sleep...");
    this_thread::sleep_for(chrono::milliseconds(2000)); 
    log_event("TEA", "Finished.");
}

// TODO: Implement cutAvocado() 
// Should log "Starting", sleep for 1000ms, and log "Finished".


// --- STOVE TASKS (Group 1: Pre-filled Example) ---

void makeEggs() {
    log_event("EGGS", "Waiting for Stove...");
    {
        lock_guard<mutex> lock{stove_lock}; 
        log_event("EGGS", "Got Stove. Cooking...");
        this_thread::sleep_for(chrono::milliseconds(3000)); 
    }
    log_event("EGGS", "Finished. Released Stove.");
}

void makeHam() {
    log_event("HAM", "Waiting for Stove...");
    {
        lock_guard<mutex> lock{stove_lock}; 
        log_event("HAM", "Got Stove. Cooking...");
        this_thread::sleep_for(chrono::milliseconds(3000)); 
    }
    log_event("HAM", "Finished. Released Stove.");
}

// --- AIRFRYER TASKS (Group 2) ---

// TODO: Implement makeHashbrowns() and makeWaffles() 
// Both should:
// 1. Log "Waiting for Airfryer..."
// 2. Use a lock_guard with the airfryer_lock (once declared)
// 3. Log "Got Airfryer. Cooking..."
// 4. Sleep for 4000ms
// 5. Log "Finished. Released Airfryer."


int main() {
    cout << "--- STARTING COMPLEX KITCHEN LOGS ---" << endl;

    // --- TODO: INITIALIZE ALL THREADS ---
    // You need threads for: Tea, Eggs, Ham, Hashbrowns, Waffles, and Avocado.
    thread t1{makeTea};
    thread t2{makeEggs};
    thread t3{makeHam};


    // --- TODO: JOIN ALL THREADS ---
    t1.join();
    t2.join();
    t3.join();


    cout << "--- ALL TASKS COMPLETE ---" << endl;

    return 0;
}