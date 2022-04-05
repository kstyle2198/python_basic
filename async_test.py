# 동기형 코드
import asyncio
import time


# def delivery(name, mealtime):
#     print(f"{name}에게 배달 완료")
#     time.sleep(mealtime)
#     print(f"{name} 식사 완료, {mealtime} 시간 소요")
#     print(f"{name} 그릇 수거 완료")


# def main():
#     delivery("Kim", 5)
#     delivery("Noh", 3)
#     delivery("Yoon", 2)


# if __name__ == "__main__":
#     start = time.time()
#     main()
#     end = time.time()
#     print(end-start)


# 비동기형 코드

async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime} 시간 소요")
    print(f"{name} 그릇 수거 완료")


async def main():
    await asyncio.gather(
        delivery("Kim", 5),
        delivery("Noh", 3),
        delivery("Yoon", 2),
    )


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end-start)
