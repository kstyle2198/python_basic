# list append & extend
# foods = ['apple', 'bread', 'noodle']
# foods.append("potato")
# print(foods)

# price = [30, 40, 50, 60]

# foods.append(price)
# print(foods)

# foods.extend(price)
# print(foods)


# **kwargs
# def getInfo(name, age, job):
#     print(name, age, job)
# info = {'name': "kim", "age": 30, "job": "developer"}
# getInfo(info)
# TypeError: getInfo() missing 2 required positional arguments: 'age' and 'job'
# getInfo(**info)


# *args
def getInfo(do, re, mi):
    print(do, re, mi)


info = [1, 2, 3]
# getInfo(info)
# TypeError: getInfo() missing 2 required positional arguments: 're' and 'mi'
getInfo(*info)
