def histogram():
    numbers = input().split()
    numbers = [int(num) for num in numbers]
    for num in numbers:
        print('*' * num)


histogram()
