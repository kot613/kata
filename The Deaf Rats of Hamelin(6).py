"""
Ката Задание
Сколько глухих крыс?

Легенда
P = Крысолов
O~ = крыса идет налево
~O = Крыса идет направо
Пример
ex1 ~O~O~O~O P имеет 0 глухих крыс

ex2 P O~ O~ ~O O~ есть 1 глухая крыса

ex3 ~O~O~O~OP~O~OO~ имеет 2 глухих крыс
"""

def count_deaf_rats(town):
    left, _, right = town.partition('P')

    def count_deaf_rats_for_side(side: str, direction: str):
        side = side.replace(' ', '')
        side_lst = [side[i:i + 2] for i in range(0, len(side), 2)]
        count = sum([1 for el in side_lst if el == direction])
        return count

    return count_deaf_rats_for_side(left, 'O~') + count_deaf_rats_for_side(right, '~O')




# def count_deaf_rat(town):
#     return town.replace(" ", "")[0::2].count("O")




print(count_deaf_rats("~O~O~O~O P"))
print(count_deaf_rats("P O~ O~ ~O O~"))
print(count_deaf_rats("~O~O~O~OP~O~OO~"))

