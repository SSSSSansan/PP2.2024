from itertools import permutations

def permutat(input_string):
    all_permutations = permutations(input_string)
    for perm in all_permutations:
        print(''.join(perm))

user_input = input()
permutat(user_input)
