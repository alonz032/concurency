
# Assignment: Concurrency & Parallelism

This assignment is divided into two core parts designed to show you how to handle multiple tasks efficiently in both C++ and Python.

---

## Part 1: Concurrency with `sleep`
**Focus:** Concurrency using non-blocking I/O

In this folder, we simulate a kitchen where resources (stoves, pans, airfryers) are limited

### Files:
* **`main.cpp`**: Multi-threaded C++. 
    * **Concepts**: `std::thread`, `std::mutex`, and `std::lock_guard`.
    * **Goal**: Implement functions that are cooperative and functions that are competitive
* **`main.py`**: Basic Asyncio.
    * **Concepts**: `async`/`await`, `asyncio.Lock`
    * **Goal**: Implement functions that are cooperative and functions that are competitive
* **`rest.py`**: Scaling up to a Restaurant
    * **Concepts**: `asyncio.Semaphore` and `asyncio.gather`.
    * **Goal**: Scale the kitchen. Manage a pool of multiple resources for a line of hungry customers.

### Step 1: main.cpp
Implement the required functions and call them appropriately in `main()`.

`TODO` comments will guide you on what to do.

### Step 2: main.py
This is the Python version of main.cpp

Implement the required functions and call them appropriately in `main()`.

`TODO` comments will guide you on what to do.

### Step 3: rest.py
For this program, we will explore having more than one shared resource. The context is that we will be opening up a restaurant and cooking meals for customers, rather than just ourselves.
Make sure to use `semaphores` to implement the multiple resources.

`TODO` comments will guide you on what to do.

When you are done implementing the functions, make sure you try with multiple customers and multiple resources.

---

## Part 2: Parallelism?
**Focus:** CPU-Bound Work and Performance Scaling.

In Part #1, we used non-blocking IO. This was perfect for simple concurrency where we used `sleep` to simulate that we were free to move onto another task. For those implementations, `sleep` was equivalent to passively waiting for a drink/dish to cook on its own. In a real program, that might be waiting for a response from a server, database, or User IO.

For this part, we will look at CPU-bound work, where instead of creating multiple threads that passively `sleep`, they thread will be actively performing work at all times.

The task each thread will be doing is counting to a very large number.

### Files:
* **`normal.py`**: A classic, sequential program. One task at a time. **Zero concurrency!**
* **`threaded.py`**: Concurrency using Python `thread`
* **`mult.py`**: Concurrency using Python `process`
* **`mult.cpp`**: Concurrency using `std::thread`

Follow the steps. You will run each program and answer questions. 

### **Short answers are fine!**  Just be sure to answer each part of the question.

### Step 1: Sequential Program
Run `normal.py`. This has one set of counting right after the other.
* **Q1:** How much time did it take for the program to finish?
* **Q2:** Why is this program non-concurrent? Can paralleism ever occur in this type of program?



### Step 2: Python Threads 
Run `threaded.py`. We are now using multiple threads to do the work.
* **Q3:** How much time did it take for the program to finish?
* **Q4:** Is this parallel?
* **Q5:** Did the time actually improve? Explain why the time did or did not change. 

### Step 3: Python Processes 
Run `mult.py`. This uses the `multiprocessing` library.
* **Q6:** How much time did it take for the program to finish?
* **Q7:** Is this parallel?
* **Q8:** Did the time actually improve? Explain why the time did or did not change.


### Step 4: C++ Implementation
Run `multi.cpp`. We are back in C++ using `std::thread`.
* **Q9:** How much time did it take for the program to finish?
* **Q10:** Is this parallel?
* **Q11:** Did the time actually improve? Explain why the time did or did not change.



### Step 5: Final Reflection 
* **Q12:** For Part #1, what is the difference between the independent tasks and the grouped tasks? What type of synchronization?
* **Q13:** In `rest.py`, what did we use instead of a `lock`? What did this let us achieve?
* **Q14:** Explain the difference in type of tasks in Part 1 vs Part 2.
* **Q15:** For Part 2, why were `normal.py` and `threaded.py` about the same speed?
* **Q16:** For Part 2, which Python file was the fastest and why?
* **Q17:** Why was only one C++ implementation necessary? 

## Submissions in a PDF
### Part 1:
Screenshots of:
- main.cpp code and output
- main.py code and output
- rest.cpp code and output
### Part 2:
- Answers to all questions Q1-Q17. Short answers are fine.
