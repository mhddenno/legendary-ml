"""
Concurrency: Concurrency is about making progress on multiple tasks, but not necessarily at the same instant. In the context of asyncio, it's achieved through asynchronous programming using coroutines and event loops. While one task is waiting for I/O (e.g., reading from a file or making a network request), the event loop can switch to another task, allowing the program to make progress on multiple activities.

Parallelism: Parallelism involves simultaneously executing multiple tasks at the same time, typically on multiple processors or cores. This is achieved using parallel programming techniques like multiprocessing. Each task runs independently and may execute in parallel, providing potential speedup for CPU-bound tasks.

asyncio is not designed for parallelism in the traditional sense. It is more suitable for I/O-bound tasks where tasks spend a significant amount of time waiting for external resources (like files, network requests, or databases). While one task is waiting, the event loop can switch to another task, making the overall program more efficient.
"""


import asyncio

async def task1() -> None:
    print("Hi here is task 1")
    print("Task 1: I am a task that takes 2 seconds to complete")
    await asyncio.sleep(2)
    print("Task 1: I am done")

async def task2() -> None:
    print("Hi here is task 2")
    print("Task 2: I am a task that takes 1 seconds to complete")
    await asyncio.sleep(1)
    print("Task 2: I am done")

async def main() -> None:
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    await asyncio.gather(t1, t2)

if __name__ == "__main__":
    asyncio.run(main())