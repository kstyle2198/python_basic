import time
from concurrent import futures
import asyncio


def cumulative(num: int):
    result = 0
    for i in range(num):
        result += i
    print("실행이 완료되었습니다.")
    return result


if __name__ == "__main__":
    targets = [300000000, 20000, 9000000, 400000, 300000]
    start = time.time()


    # with futures.ThreadPoolExecutor() as executor:
    #     results = [executor.submit(cumulative, num) for num in targets]
    #     print(results)
    #     for f in futures.as_completed(results):
    #         print(f.result())

####################################
    result = [cumulative(i) for i in targets]
    print(result)
####################################

    end = time.time()
    print(end-start)
