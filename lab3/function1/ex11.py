def is_polindrome():
    string = input()
    rev = ''.join(reversed(string)) 
    if string == rev :
        return "Yes"
    else:
        return "No"
        
result = is_polindrome()
print(result)