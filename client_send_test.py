import asyncio
import sys
import time

from pandablocks.asyncio import AsyncioClient
from pandablocks.commands import Put

TIME_LIST = []


# def timer(func):
#     async def process(func, *args, **params):
#         return await func(*args, **params)

#     async def helper(*args, **params):
#         print(f"{func.__name__}.time")
#         start = datetime.datetime.now()
#         print(start)

#         result = await process(func, *args, **params)

#         finish = datetime.datetime.now()

#         TIME_LIST.append(finish - start)

#         print(">>> Time elapsed - ", finish - start)
#         return result

#     return helper


async def send_pgen():
    # Create a client and connect the control and data ports
    async with AsyncioClient(sys.argv[1]) as client:
        # Put to 2 fields simultaneously
        for x in range(0, 10):
            start = time.time()
            print(start)
            await asyncio.gather(
                client.send(Put("BITS.A", 1)),
            )
            finish = time.time()
            TIME_LIST.append(finish - start)


if __name__ == "__main__":
    asyncio.run(send_pgen())

    print(TIME_LIST)
