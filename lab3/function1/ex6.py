def reverse_words(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))

    return reversed_words

user_input = input()
result = reverse_words(user_input)
print(result)
