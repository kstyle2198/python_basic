import pandas as pd

df = pd.read_excel("./files/계층형데이터.xlsx")
ddf = df[["level3", "level4", "level5", "level6"]]
# print(ddf)
t_row = ddf.iloc[0:10]
print(t_row)
for idx, row in t_row.iterrows():
    # print(idx, row)
    print(row.values)
    for i in row.values:
        print(i)













# print(type(df.iloc[0:1]["level4"].values[0]))
# print(str(df.iloc[0:1]["level4"].values[0]) == "nan")
# for i in range(len(df[df["level3"] == "조건"]["level4"])):
#     print(i)

# exit()

# total_cnt = len(df["level3"])
# num1 = 1
# for i in range(total_cnt):
#     target1 = df.iloc[i:i+1]["level3"].values[0]
#     if i == 0:
#         print(f"{num1}조:{i}:{target1}")
#         num1 += 1

#         num2 = 1
#         for k in range(len(df[df["level3"] == target1]["level4"])):
#             target2 = df.iloc[k:k+1]['level4'].values[0]
#             if k == 0 and str(target2) != "nan":
#                 print(f"--{num2}항:{k}:{target2}")
#                 num2 += 1
#             elif k != 0 and str(target2) != "nan":
#                 pre_target2 = df.iloc[k-1:k]["level4"].values[0]
#                 if target2 != pre_target2:
#                     print(f"--{num2}항:{k}:{target2}")
#                     num2 += 1

#     elif i != 0:
#         pre_target1 = df.iloc[i-1:i]["level3"].values[0]
#         if target1 != pre_target1:
#             print(f"{num1}조:{i}:{target1}")
#             num1 += 1

#             num2 = 1
#             for k in range(len(df[df["level3"] == target1]["level4"])):
#                 target2 = df.iloc[k:k+1]['level4'].values[0]
#                 if k == 0 and str(target2) != "nan":
#                     print(f"--{num2}항:{k}:{target2}")
#                     num2 += 1
#                 elif k != 0 and str(target2) != "nan":
#                     pre_target2 = df.iloc[k-1:k]["level4"].values[0]
#                     if target2 != pre_target2:
#                         print(f"--{num2}항:{k}:{target2}")
#                         num2 += 1
