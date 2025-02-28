import asyncio
import datetime
import sys

from pandablocks.asyncio import AsyncioClient
from pandablocks.commands import Put

TIME_LIST = []


def timer(func):
    async def process(func, *args, **params):
        return await func(*args, **params)

    async def helper(*args, **params):
        print(f"{func.__name__}.time")
        start = datetime.datetime.now()
        print(start)

        result = await process(func, *args, **params)

        finish = datetime.datetime.now()

        TIME_LIST.append(finish - start)

        print(">>> Time elapsed - ", finish - start)
        return result

    return helper


@timer
async def send_pgen():
    # Create a client and connect the control and data ports
    async with AsyncioClient(sys.argv[1]) as client:
        # Put to 2 fields simultaneously
        await asyncio.gather(
            client.send(Put("BITS.A", 1)),
            client.send(Put("PGEN1.TABLE", [str(x) for x in range(0, 262144)])),
            client.send(Put("PGEN1.TABLE", [str(x) for x in range(262144, 524288)])),
            client.send(Put("PGEN1.TABLE", [str(x) for x in range(524288, 786432)])),
            client.send(Put("PGEN1.TABLE", [str(x) for x in range(786432, 1000000)])),
            client.send(Put("BITS.A", 0)),
        )


if __name__ == "__main__":
    for x in range(0, 10):
        asyncio.run(send_pgen())

    print(TIME_LIST)
