import random

words = ["apple", "banana", "orange", "computer",
         "impression", "tennis", "lemon", "mom", "desk"]

정답 = random.sample(words, 1)[0]
정답_리스트 = list(정답)
# print(" ".join(정답_리스트))
answer_sheet = "_"*len(정답)
answer_sheet_list = list(answer_sheet)
print(answer_sheet_list)


while True:

    input_value = input()
    if input_value in 정답_리스트 and input_value not in answer_sheet_list:
        print("단어가 포함되어 있습니다.")
        n = 0
        for i in 정답_리스트:
            if i == input_value:
                answer_sheet_list[n] = i
            n += 1
        print(" ".join(answer_sheet_list))
        남은정답개수 = answer_sheet_list.count("_")
        print(f"남은정답개수 : {남은정답개수}")

        if 남은정답개수 == 0:
            print("성공")
            break

    elif input_value in answer_sheet_list:
        print("중복응답입니다.")

    else:
        print("틀림")
