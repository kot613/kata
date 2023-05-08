"""
Учитывая строку слов, вам нужно найти слово с наивысшим баллом.
Каждая буква слова оценивается в зависимости от ее положения в алфавите: a = 1, b = 2, c = 3 и т. д.
Вам нужно вернуть слово с наивысшим баллом в виде строки.
Если два слова оцениваются одинаково, верните слово, которое появляется первым в исходной строке.
Все буквы будут строчными, и все входные данные будут действительными.
"""



def high(llst):
    lst = llst.split()
    CONST = 96
    ans = {}
    for word in lst:
        key = 0
        for char in word:
            key += ord(char) - CONST
        if not ans.get(key):
            ans[key] = word
    print(ans[max(ans)])

def high1(x):
    print(max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k)))






s = 'man i need a taxi up to ubud'
high1(s)
s = 'aa b'
high1(s)
s = 'b aa'
high1(s)