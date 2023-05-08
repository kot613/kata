"""
Реализуйте функцию unique_in_order, которая принимает в качестве аргумента последовательность и
возвращает список элементов без каких-либо элементов с одинаковым значением рядом друг с другом
и с сохранением исходного порядка элементов.

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""


def unique_in_order(lst):
    ans = []
    prev = None
    for char in lst[0:]:
        if char != prev:
            ans.append(char)
            prev = char
    return ans
