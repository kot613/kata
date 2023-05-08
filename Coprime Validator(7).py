"""
Напишите программу, которая определяет взаимно просты ли два заданных числа. Пара чисел взаимно проста,
если их наибольший общий делитель равен 1.

Входными данными всегда будут два положительных целых числа от 2 до 99.
"""
def prime_num(num:int):
    ans = [i for i in range(1, num + 1) if num % i == 0]
    return ans


def are_coprime(n,m):
    lst_n = prime_num(n)
    lst_m = prime_num(m)
    ans = True if set(lst_n) & set(lst_m) == {1} else False
    return ans




are_coprime(20, 27)