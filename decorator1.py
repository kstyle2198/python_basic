'''
decorator를 한마디로 이야기하자면, 대상함수를 wrapping하고, 이 wrapping된 함수의 앞뒤에
꾸며질 구문들을 정의해서 손쉽게 재사용 가능하게 해주는 것

예컨데.. 단순한 프린트 메인함수의 앞뒤로 해당 문장을 출력하기 전과 후의 일시를 출력하고 싶다면???
'''

import datetime

# * 쌩으로 한다면..
# def main():
#     print(datetime.datetime.now()) # 데코부분
#     print("Main Function Start")
#     print(datetime.datetime.now())  # 데코부분

# main()

# 데코 부분을 별도 함수(이 함수는 메인함수를 변수로 받는다)로 만든후 데코레이터로 사용


def checkTime(func):
    def deco_func(*args):
        print(datetime.datetime.now())  # 데코부분
        func(*args)
        print(datetime.datetime.now())  # 데코부분
        print("꾸며질 내용을 추가합니다.")
    return deco_func


@checkTime
def main(*args):
    for arg in args:
        print(f"Main Function Start by "+arg)


if __name__ == "__main__":
    main("kim", "yoon")
