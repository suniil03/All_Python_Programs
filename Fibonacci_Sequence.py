def fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return (fibonacci(num-1) + fibonacci(num-2))

terms = int(input("Enter the number of terms: "))
if terms < 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    for i in range(0, terms + 1):
        print(fibonacci(i), end=" ")