"""Homework 5: Downloading multiple files using async"""
import asyncio
import aiohttp
import time
import os
import sys
from get_files import get_files_list


async def get_url(url, path, session, sem_number):
    name = url.split('/')[-1]
    filename = os.path.join(path, name)
    sem = asyncio.Semaphore(sem_number)
    async with sem:
        async with session.get(url) as response:
            with open(filename, 'wb') as fd:
                print("Updating {}".format(filename))
                async for data in response.content.iter_chunked(4096):
                    fd.write(data)
    return 'Successfully downloaded ' + filename


async def main(urls, path, sem_number):
    async with aiohttp.ClientSession() as session:
        tasks = [get_url(url, path, session, sem_number) for url in urls]
        return await asyncio.gather(*tasks)

if __name__ == '__main__':
    links = get_files_list()

    sem_number = 0
    if len(sys.argv) == 2:
        try:
            sem_number = int(sys.argv[1])
        except Exception:
            print("Wrong type of argument")
            sys.exit(1)
    else:
        sem_number = 2

    start_time = time.time()
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(main(links, '/tmp', sem_number))
    loop.close()
    print("\n".join(result))
    print("Final time: {:.2f}".format(time.time() - start_time))
