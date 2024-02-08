def calculate_running_average(numbers):
    total = 0
    averages = []
    for i, num in enumerate(numbers, start=1):
        total += num
        averages.append(total / i)
    return averages

numbers = [int(x) for x in input().split()]
result = calculate_running_average(numbers)
print(result)
