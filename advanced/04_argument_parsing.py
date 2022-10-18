import sys
def myfunc(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(kwargs['arg_one'])
    print(kwargs['arg_two'])
    print(kwargs['arg_three'])

myfunc("hello", 30, arg_one=37, arg_two={"name": "kelly", "job":"DE"}, arg_three="You can do it")

# argv : argument vector
print(sys.argv[0])
# print(sys.argv[1])

# Usage: file.py filename
filename = sys.argv[1]
message = sys.argv[2]

with open(filename, 'w+') as f:
    f.write(message)

import getopt
opts, args = getopt.getopt(sys.argv[1: ], "f:m:", ['filename', "message"])

print(opts)
print(args)


for opt, arg in opts:
    if opt == '-f':
        filename = arg
    elif opt == 'm':
        message = arg
with open (filename, 'w+') as f:
    f.write(message)