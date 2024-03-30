def fib(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

def fibo(number):
    fib_gen = fib(number)
    for fib_num in fib_gen:
        pass
    return fib_num

input_number = int(input())
fibonacci_number = fibo(input_number)
print(fibonacci_number)
