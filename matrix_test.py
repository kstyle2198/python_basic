import numpy as np

target = [
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 1, 1]
]

# print(target)

for i in target:
    print(i)
    for k in i:
        print(f"index : {i.index(k)}, value : {k}")
