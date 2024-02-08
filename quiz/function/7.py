def word_frequency(text):
    words = text.split()
    frequency = {}
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

input_text = input()
result = word_frequency(input_text)
print(result)
