def snak(snake):
    s = snake.split('_')
    camel = s[0] + ''.join(word.title() for word in s[1:])  
    return camel

snake_string = input()
camel_string = snak(snake_string)
print(camel_string)