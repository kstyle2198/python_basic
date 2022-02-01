import sys

# my_list = [i for i in range(100)]
# print(my_list)
# print(sys.getsizeof(my_list))

# print("-"*20)

my_generator = (i for i in range(100))
print(my_generator)
print(sys.getsizeof(my_generator))

for k in my_generator:
    print(k)
