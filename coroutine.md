# Coroutine

### 1. 일반 정의
코루틴은 서브 루틴을 일시 정지학 재개할 수 있는 구성요소를 말한다. 쉽게 말해 필요에 따라 일시 정지할 수 있는 함수를 의미한다.

* 통상 서브루틴(일반함수)은 하나의 진입점과 하나의 탈출점을 갖는다.
* 코루틴은 다양한 진입점과 다양한 탈출점을 가지고 있다.

#### 1. 비동기 함수 예제
```python
import time

def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    time.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime}시간 소요...")
    print(f"{name} 그릇 수거 완료")


def main():
    delivery("A", 1)
    delivery("B", 2)
    delivery("C", 3)


if __name__ == "__main__":
    start = time.time()
    print(main())  # None
    end = time.time()
    print(end - start)

```

#### 2. 동기 함수 예제
```python
import time
import asyncio


async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime}시간 소요...")
    print(f"{name} 그릇 수거 완료")
    return mealtime


async def main():

    result = await asyncio.gather(
        delivery("A", 1),
        delivery("B", 2),
        delivery("C", 3),
    )

    print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)

```

