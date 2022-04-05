import requests
import time
import threading
from concurrent.futures import ThreadPoolExecutor

#  multi threading을 사용한 비동기적 처리 방식

def fetcher(params):
    print(params)
    session = params[0]
    url = params[1]
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://naver.com", "https://google.com", "https://daum.net"]

    executor = ThreadPoolExecutor(max_workers=1)

    with requests.Session() as session:
        # result = [fetcher(session, url) for url in urls]
        # print(result)
        executor.map(fetcher, urls)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end-start)
