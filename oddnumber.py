lower = int(input())
upper = int(input())

for n in range(lower,upper + 1):
   # prime numbers are greater than 1
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)
