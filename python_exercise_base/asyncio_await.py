import asyncio


async def hello():
    print('Hello,World!')
    r = await asyncio.sleep(2)
    print('Hello,Again')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [hello(), hello(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()