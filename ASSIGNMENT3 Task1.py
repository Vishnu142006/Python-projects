n = int(input())
def factorial(n):
    if 0<= n < 2:
        print(f"The factorial of {n} is 1")
    else:
        fact= 1
        for i in range(2,n+1):
            fact = fact * i
        print(f"The factorial of {n} is {fact}")

factorial(n)





