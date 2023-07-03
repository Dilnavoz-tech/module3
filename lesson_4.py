# def massiv(num: list):
#     for i in range(len(num)):
#         arr, sum = [], 0
#         for j in range(i+1):
#             sum += num[j]
#             arr.append(sum)
#     return arr
#
#
# aa = [1, 2, 3, 4, 5]
# print(massiv(aa))


import time
from datetime  import date
import datetime

now = datetime.datetime.now()
now_date = now.strftime("%Y-%m-%d")

print(date.today())
print(date.fromisoformat(now_date) - date.fromisoformat("2014-02-28"))

print(date.fromtimestamp(0))


