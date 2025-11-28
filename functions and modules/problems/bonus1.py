def fib(n):
    if n == 0 or n == 1:   # base case
        return n
    else:
        return fib(n - 1) + fib(n - 2)   # recursive case

print(fib(7))
