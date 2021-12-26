import sys


def sumList(num):
    lst = []
    for i in range(num):
        lst.append(i)
    # print(lst)
    return sum(lst)


result = sumList(1000000)
print(result)
print(sys.getsizeof(result))

print("-"*20)


def sumGen(num):
    for i in range(num):
        yield i


gen_result = sum(sumGen(1000000))

# for n in gen_result:
#     print(n)

print(gen_result)
print(sys.getsizeof(gen_result))
