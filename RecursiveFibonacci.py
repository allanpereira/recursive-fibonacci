def fibonacci(n):
    if n >= 2 :
        return fibonacci(n-2) + fibonacci(n-1)
    else:
        return n

number = int(input("Enter the number: "))
print ("The nth Fibonacci number is %d" % (fibonacci(number)))