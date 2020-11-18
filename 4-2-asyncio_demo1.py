import asyncio
import time


async def job(t):
    print('Start job', t)
    await asyncio.sleep(t) # 添加一个等待点
    print('Job', t, 'takes', t, 's')


async def main(loop):
    tasks = [loop.create_task(job(t)) for t in range(1, 3)]
    await asyncio.wait(tasks) # 添加一个等待点


t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop)) # 直到所有等待点都完成
loop.close()
print('Async total time:', time.time() - t1)
