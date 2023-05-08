"""
Все знают парольные фразы. Можно выбрать фразы-пароли из стихов, песен, названий фильмов и т. д.,
но часто их можно угадать из-за общих культурных отсылок. Вы можете усилить свои парольные фразы разными способами.
Один из них следующий:
1---выберите текст заглавными буквами, включая или не включая цифры и неалфавитные символы,
сдвинуть каждую букву на заданное число, но преобразованная буква должна быть буквой (круговой сдвиг),
2---замените каждую цифру ее дополнением до 9,
3---сохранить, например, небуквенные и нецифровые символы,
4---в нижнем регистре каждая буква в нечетной позиции, в верхнем регистре каждая буква в четной позиции
(первый символ находится в позиции 0),
5---перевернуть весь результат.

Example:
your text: "BORN IN 2015!", shift 1
1 + 2 + 3 -> "CPSO JO 7984!"
4 "CpSo jO 7984!"
5 "!4897 Oj oSpC"

"""

def play_pass(s, n):
    lst = [chr(x) for x in range(65, 91)]
    # step 1+2+3
    ans = ''
    for char in s:
        if char.isalpha():
            char_index = lst.index(char)
            ans += lst[char_index + n - len(lst)] if char_index + n >= len(lst) else lst[char_index + n]
        elif char.isnumeric():
            ans += str((9 - int(char)))
        else:
            ans += char
    # step 4
    qwerty = ''.join([char.lower() if char.isalpha() and i % 2 != 0 else char for i, char in enumerate(ans)])
    # step 5
    ans = qwerty[::-1]
    return ans




print(play_pass("I LOVE YOU!!!", 1))
print(play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2))
print(play_pass("BORN IN 2015!", 1))