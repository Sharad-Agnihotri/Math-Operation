import sys

if len(sys.argv) == 2:
    num = int(sys.argv[1])
else:
    num = 3


if num % 2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")


for i in range(2, num):
    if num % i == 0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")
