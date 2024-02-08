def prime_n(numbers):
    numbers1 = []
    for i in range(0, len(numbers)):
        for x in range(2, numbers[i]):
            if numbers[i] == 2:
                numbers1.append(numbers[i])
                break
            if numbers[i] % 2 != 0:
                numbers1.append(numbers[i])
                break
            else:
                continue
    print(numbers1)
        
numbers = [int(x) for x in input().split()]



prime_n(numbers)