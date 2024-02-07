def filter_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

input_numbers = int(input())
result = [num for num in input_numbers if filter_prime(num)]
print(result)
