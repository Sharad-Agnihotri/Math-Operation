import sys

if len(sys.argv) == 2:
    num = int(sys.argv[1])
else:
    num = 3

if num % 2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")


if num <= 1:
    print("It is not a prime number")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")
