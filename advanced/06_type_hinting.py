# 동적 타입 - 런타임전까지 type을 모른다.


def myfunc(mypara: int) -> str:
    print(f"para value: {mypara}")

    return f"{mypara+10}"

def otherfunc(otherpara: str):
    print(otherpara)
# TypeError: can only concatenate str (not "int") to str
# myfunc("Hello World")


def thefunc(thepara: list):
    for value in thepara:
        print(value)

print(f"return: {myfunc(1)}")

otherfunc("Hello World")

thefunc([1,2,3,4,5])