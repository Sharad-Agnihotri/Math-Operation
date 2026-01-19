import sys

if len(sys.argv)==2:
    num=int(sys.argv[1])
else:
    num=3

if num%2==0:
    print("It is a even number")
else:
    print("It is a odd number")

for i in range(1,11):
    if num%i==0:
        print("it is not a prime number")
    else:
        print("It is a prime number")
