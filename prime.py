number = int(input())
if number < 1000:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print("yes")
else:
    print("no")
