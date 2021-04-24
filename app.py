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


def f(x, y): return x*y


# try:
#     s = "hello world"
#     i = int(s)
# except ValueError:
#     print("Not a number")

def division(a, b):
    if b == 0:
        raise ZeroDivisionError()
    return a/b


# div = division(1, 0)

class Panther:
    def run(self):
        print("Panther Running")


class Jaguar:
    def run(self):
        print("Jaguar Running")


class Whale:
    def swim(self):
        print("Whale swimming")


randomAnimals = (Panther, Jaguar, Whale)

# for animal in randomAnimals:
#     animal.run() #whale has no attribute run, but other methods were called


class Human:
    humanCount = 0

    def __init__(self, name="Noname", age="0"):
        self.name = name
        self.age = age
        Human.humanCount += 1

    def __str__(self):
        return f"This human is called {self.name} and his age is {self.age}"

    def __eq__(self, other):
        print("eq is called")
        return self.name == other.name and self.age == other.age

    def getAge(self):
        return self.age

    def printAge(self):
        print("Age of super {self.age}")

# print(someGuy) #calls __str__ function


someGuy = Human("Josh", 33)
theSameGuy = Human("Josh", 33)

# print(someGuy == theSameGuy)  # true because eq is called

# 2 da init zwemal aufgerufen insg im ganzer App
hCount = Human.humanCount


class Student(Human, Whale):
    def __init__(self, name, age):
        super().__init__(name, age)

    def learn(self):
        print("Student is learning")

    def printAge(self):  # überschriebene Methode
        print(f"Student is {super().getAge()}")


someStudent = Student("Doe", 21)
studentsName = someStudent.name  # Doe, name was inherited

# someStudent.swim() #inherithed from whale


class Point:
    def __init__(self, x, y):  # it has to be written with _x, otherwise it wont work
        self._x = x
        self._y = y

    def set_x(self, x):
        self._x = x
        print("x setter new value: ", x)

    def get_x(self):
        print("X getted")
        return self._x

    x = property(get_x, set_x)


# p = Point(5, 5)
# p.x  # get x
# p.x = 10  # set x

print(studentsName)
