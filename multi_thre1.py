import requests
import time
import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import os

#  multi threading을 사용한 비동기적 처리 방식


def fetcher(params):
    # print(params)
    session = params[0]
    # print(session)
    url = params[1]
    # print(url)
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://naver.com", "https://google.com", "https://daum.net"]

    executor = ThreadPoolExecutor(max_workers=3)
    # executor = ProcessPoolExecutor(max_workers=3)

    with requests.Session() as session:
        # result = [fetcher(session, url) for url in urls]
        # print(result)
        params = [(session, url) for url in urls]
        results = list(executor.map(fetcher, params))
        # print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end-start)
