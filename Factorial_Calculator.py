def factorial(num):
    if(num==1 or num==0):
        return 1 
    else:
        return num * factorial(num - 1)


n = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {n} is {factorial(n)}")
