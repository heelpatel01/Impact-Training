def fibonacci_series(n):
    fib_series = [0, 1]
    
    while fib_series[-1] + fib_series[-2] <= n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    
    return fib_series

n = int(input("Enter the value of n: "))

result = fibonacci_series(n)
print("Fibonacci Series up to", n, ":", result)




