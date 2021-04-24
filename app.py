import math

x = 1
y = 5e1

s = """
Ja moin wie geht es ezch
"""
arr = [1, "string", 5, "moin"]
arrConst = (2, 5, 3)
arrConst = (2, 7, 7, 4)  # what wird trotzdem uberschrieben

partArr = arr[-1]  # moin
partArr2 = arr[1:3]  # string, 5

arr2 = [4, 5, 9]
arr3 = [6, 8, 3]

arrMulti = arr2 * 5  # [4, 5, 9, 4, 5, 9, 4, 5, 9, 4, 5, 9, 4, 5, 9]
arrAdd = arr2 + arr3
# minArr = min(arr)  # err
arr.append("haha")  # haha am ende
arrLen = len(arr2)  # 3

dic = {"key1": "value1", "key2": "value2"}
dicKeys = dic.keys()
dicItems = dic.items()

conv = str(43)
conv2 = type(conv)

if conv == "44":
    print("is 44")
elif conv == "55":
    print("is 55")


arr4 = [4, 5, 9]
equal = arr2 == arr4  # true
equal2 = arr2 is arr4  # false

# for i in range(len(arr4)):
#     print(arr4[i])

# for el in arr4:
#     print(el)

arr5 = [i*2 for i in range(10)]  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
arr6 = [el+10 for el in arr4]  # [14, 15, 19]
dic2 = {i: i*2 for i in range(10)}
# => {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}


def multiply(x, y):
    return x*y


def someNumbers():
    return [1, 2, 3, 4, 5]


u, i, o, p, h = someNumbers()  # 1,2,3,4,5

# print(math.sin(math.pi))

print(u, i, o, p, h)
