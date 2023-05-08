"""
Задача о максимальной сумме подмассива состоит в нахождении максимальной суммы непрерывной подпоследовательности в
массиве или списке целых чисел:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# должно быть 6: [4, -1, 2, 1]
Простой случай — это когда список состоит только из положительных чисел, а максимальная сумма — это сумма всего массива.
Если список состоит только из отрицательных чисел, вместо этого верните 0.

Пустой список считается имеющим нулевую наибольшую сумму. Обратите внимание,
что пустой список или массив также является допустимым подсписком/подмассивом.
"""


def maxSubArraySum(arr, size):
    max_till_now = arr[0]
    max_ending = 0

    for i in range(0, size):
        max_ending = max_ending + arr[i]
        if max_ending < 0:
            max_ending = 0
        elif (max_till_now < max_ending):
            max_till_now = max_ending
    return max_till_now






def max_sequence(arr):
    if all([True if el > 0 else False for el in arr]):
        return sum(arr)
    elif all([True if el < 0 else False for el in arr]):
        return 0
    elif not arr:
        return 0
    else:
        return maxSubArraySum(arr, len(arr))




print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sequence([]))