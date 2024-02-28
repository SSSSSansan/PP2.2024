import re
snake = input()
capital = snake.upper()
camel = ""
i = 0
while(i != len(snake)):
    if(snake[i] == '_'):
        camel = camel + capital[i+1]
        i = i + 2
    else:
        camel = camel + snake[i]
        i = i + 1

print(camel)