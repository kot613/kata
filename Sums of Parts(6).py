"""
Функция parts_sums (или ее варианты на других языках) примет в качестве параметра список ls и вернет список сумм
его частей, как определено выше.

"""

def parts_sums(ls):
    sums = [sum(ls)]
    for i in ls:
        sums.append(sums[-1] - i)
    return sums
    # your code



print(parts_sums([0, 1, 3, 6, 10]))
print(parts_sums([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]))