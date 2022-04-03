class Calculator1:
    '''
    Author : Kim
    Features : 리스트 형태의 복수의 값을 연산하는 계산기
    '''

    def __init__(self):
        return None

    def add(self, lst):
        result = 0
        for var in lst:
            result += var
        return result

    def subtract(self, lst):
        result = 0
        for var in lst:
            if lst.index(var) == 0:
                result = var
            else:
                result -= var
        return result

    def multiple(self, lst):
        result = 1
        for var in lst:
            result *= var
        return result

    def divide(self, lst):
        result = 1
        for var in lst:
            if lst.index(var) == 0:
                result = var
            else:
                result /= var
        return result


cal1 = Calculator1()
lst1 = [i for i in range(1, 100)]

# print(cal1.add(lst1))
# print(cal1.subtract(lst1))
# print(cal1.multiple(lst1))
# print(cal1.divide(lst1))

print(Calculator1.__dict__)
print(dir(Calculator1))
