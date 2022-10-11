# https://www.youtube.com/watch?v=lox29cXvwnk&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=3
import sys

# generator lazy execution
def mygenerator(x):
    for x in range(x):
        yield  x ** 3

values = mygenerator(10)

print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))

print(f"size: {sys.getsizeof(values)}")
for x in values:
    print(x)

print(f"size: {sys.getsizeof(values)}")


def infinite_sequence():
    result = 1
    while True:
        yield  result
        result *= 5
val = infinite_sequence()
print(f"size: {sys.getsizeof(val)}")
print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))

print(f"size: {sys.getsizeof(val)}")

gen_obj = []
gen_obj = (num for num in range(100))

num_list = []
for num in range(100):
    num_list.append(num)

print(f"type(gen_obj): {type(gen_obj)}, type(num_list): {type(num_list)}")
print(f"sys.getsizeof(gen_obj): {sys.getsizeof(gen_obj)}, sys.getsizeof(num_list): {sys.getsizeof(num_list)}")