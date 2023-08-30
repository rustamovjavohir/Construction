import asyncio
import datetime
from pprint import pprint
from time import sleep
import httpx
from datetime import datetime
import aiohttp
import requests


async def main():
    task = asyncio.create_task(other_func())
    print('hello')
    print('world')
    await task


async def other_func():
    print('1')
    await asyncio.sleep(1)
    print('2')


async def func2():
    print("Salom")


async def _send_request(api_path):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=api_path) as response:
            return await response.json()


async def _send_get_request(api_path):
    async with httpx.AsyncClient(verify=False, timeout=60) as client:
        try:
            return await client.get(url=api_path)
        except Exception as ex:
            print(ex)
            return 0


def sync_send_request(api_path):
    return requests.get(url=api_path)


async def send_multiple_requests(api_url):
    task1 = asyncio.create_task(_send_get_request(url))
    task2 = asyncio.create_task(_send_get_request(url))
    task3 = asyncio.create_task(_send_get_request(url))
    task4 = asyncio.create_task(_send_get_request(url))
    task5 = asyncio.create_task(_send_get_request(url))
    task6 = asyncio.create_task(_send_get_request(url))
    task7 = asyncio.create_task(_send_get_request(url))
    task8 = asyncio.create_task(_send_get_request(url))

    await task6
    await task7
    await task8

    return await task1, await task2, await task3, await task4, await task5


async def functions_togather(api_url):
    return await asyncio.gather(
        _send_get_request(api_url),
        _send_get_request(api_url),
        _send_get_request("api_url"),
        _send_get_request(api_url),
        _send_get_request(api_url),
        _send_get_request(api_url),
    )


async def gater_wait(delay):
    return await asyncio.gather(
        wait(delay),
        wait(delay),
        wait(delay),
        wait(delay),
        wait(delay),
        wait(delay),
    )


async def wait(delay: int):
    await asyncio.sleep(delay)
    return delay


async def more_async_func(count, api_url):
    _list = []
    for i in range(count):
        _list.append(await _send_get_request(api_url))

    return _list


if __name__ == '__main__':
    start_time = datetime.now()
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    # res = asyncio.run(send_multiple_requests(url))
    res = asyncio.run(functions_togather(url))
    # res = asyncio.run(gater_wait(1))
    # res = asyncio.run(more_async_func(10, url))
    print(res)
    # response = asyncio.run(_send_get_request(url))
    # response3 = sync_send_request(url)
    # response2 = asyncio.run(_send_get_request(url))
    # pprint(response.json())
    print(datetime.now() - start_time)
    # asyncio.run(func2())
    # asyncio.run(main())
