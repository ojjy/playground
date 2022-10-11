# double underscore __ == dunder -> 객체에서 특별한 행위를 했을때 내부적으로 호출하는 메소드 + 의 경우 __add__()호출

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Object is being deconstructed")

p = Person("Kelly", 35)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

v1 = Vector(10, 20)
v2 = Vector(50, 50)
# v3 = v1 + v2 # __add__함수를 정의하지 않은 상태에서 두 객체를 더하면 에러가 발생
# TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'
# __init(), __del__ 명시적으로 호출하지 않았지만 객체가 생성되고 소멸되는 과정에서 자동으로 호출



class Vector1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector1(self.x+other.x, self.y+other.y)

    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"

    def __call__(self):
        return f"{self} obj CALLED"

v3 = Vector1(10, 20)
v4 = Vector1(50, 50)
v5 = v3 + v4
print(v3.x, v3.y)
print(v5())