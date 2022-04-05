import requests
import time
import aiohttp
import asyncio


# coroutine을 사용하지 않는 방식.. 동기적 처리
# def fetcher(session, url):
#     with session.get(url) as response:
#         return response.text


# def main():
#     urls = ["https://naver.com", "https://google.com", "https://daum.net"]

#     with requests.Session() as session:
#         result = [fetcher(session, url) for url in urls]
#         print(result)


# if __name__ == "__main__":
#     start = time.time()
#     main()
#     end = time.time()
#     print(end-start)


# coroutine을 사용하는 방식.. 비동기적 처리
async def fetcher(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = ["https://naver.com", "https://google.com", "https://daum.net"]

    async with aiohttp.ClientSession() as session:
        # result = await fetcher(session, urls[0])
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end-start)
