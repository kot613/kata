"""
Завершите метод, который определит минимальное количество монет, необходимое для внесения сдачи на заданную сумму в
американской валюте.

Используемые монеты будут полудолларов, четвертаков, десятицентовиков, пятицентовых монет и пенни номиналом 50 центов,
25 центов, 10 центов, 5 центов и 1 цент соответственно. Они будут представлены символами H, Q, D, N и P (символы в Ruby,
строки на других языках)

Переданный аргумент будет целым числом, представляющим значение в центах. Возвращаемое значение должно быть
хешем/словарем/объектом с символами в качестве ключей и количеством монет в качестве значений.
Монеты, которые не используются, не должны включаться в хэш. Если переданный аргумент равен 0,
то метод должен возвращать пустой хэш.

Примеры
make_change(0) #--> {}
make_change(1) #--> {"P":1}
make_change(43) #--> {"Q":1, "D":1, "N":1, "P":3}
make_change(91) #--> {"H":1, "Q":1, "D":1, "N":1, "P":1}
H = 50,
Q = 25,
D = 10,
N = 5
P = 1
"""


def make_change(amount):
    money = {50: 'H', 25: 'Q', 10: 'D', 5: 'N', 1: 'P'}
    money_nom = [50, 25, 10, 5, 1]

    def dct(coins, amount):
        char_coins = money[coins]
        count_coins = amount // coins
        amount -= count_coins * coins
        if count_coins:
            return char_coins, count_coins, amount
        return False, False, amount

    ans = {}
    for coin in money_nom:
        char_coins, count_coins, amount = dct(coin, amount)
        if char_coins:
            ans[char_coins] = count_coins
    return ans


# print(make_change(91))
print(make_change(43))

# your code here
