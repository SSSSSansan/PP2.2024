import time
def square(x,y):
    x1 = x ** (1/2)
    time.sleep(y/1000)
    print(f'Square root of {x} after {y} miliseconds is {x1}')

x = int(input())
y = int(input())
square(x,y)