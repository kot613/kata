def two_sum(numbers, target):
    for i, value_i in enumerate(numbers):
        for j, value_j in enumerate(numbers[i + 1:]):
            if value_i + value_j == target:
                return [i, j + i + 1]


print(two_sum([1, 2, 3], 4))
print(two_sum([1234, 5678, 9012], 14690))
print(two_sum([2, 2, 3], 4))


