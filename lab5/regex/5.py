import re

def match(text):
    x = 'a.*?b$'
    if re.search(x, text):
        print('Found a match')
    else:
        print('Not mached')
match(input())