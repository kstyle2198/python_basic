
names = ["홍길동", "김종배", "김윤지"]


for name in names:
    with open(f"files/{name}.txt", "w", encoding='utf-8') as f:
        # f.write(f'{name}를 찾습니다.')

        contents = f"""
안녕하세요.
제 이름은 {name}입니다.
만나서 반갑습니다.

   - {name}드림 -
"""
        f.write(contents)


'''
with open("filename.txt", "w", encoding="utf-8") as f:
    f.write("contents")

'''
