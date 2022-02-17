# print("C:\my_develop2\python_basic")
# print("C:\\my_develop2\\python_basic")

print("Python", "Java", sep="+", end=" ")
print("test1")


scores = {"math": 80, "english": 90, "coding": 95}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")


for num in range(10):
    print("대기번호 : "+str(num).zfill(3))
