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