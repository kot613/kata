"""
Реализуйте алгоритм псевдошифрования, который для заданной строки S и целого числа N объединяет все символы с
нечетным индексом S со всеми символами с четным индексом S, этот процесс должен быть повторен N раз.

Примеры:

зашифровать("012345", 1) => "135024"
зашифровать("012345", 2) => "135024" -> "304152"
зашифровать("012345", 3) => "135024" -
> "304152" -> "012345"

зашифровать("01234", 1) => "13024"
зашифровать("01234", 2) => "13024" -> "32104"
зашифровать("01234", 3) => "13024" -> "32104" -> "20314"
Вместе с функцией шифрования вы также должны реализовать функцию дешифрования, которая меняет процесс.

Если строка S является пустым значением или целое число N не является положительным,
вернуть первый аргумент без изменений.
"""

def encrypt(text, n):
    if n > 0:
        for _ in range(n):
            first, second = '', ''
            for i, value in enumerate(text):
                if i % 2 == 0:
                    first += value
                else:
                    second += value
            text = second + first
    return text


def decrypt(encrypted_text, n):
    if n > 0:
        for _ in range(n):
            first, second = encrypted_text[:len(encrypted_text)//2], encrypted_text[len(encrypted_text)//2:]
            encrypted_text = ''
            while True:
                if second:
                    encrypted_text += second[0]
                    second = second[1:]
                if first:
                    encrypted_text += first[0]
                    first = first[1:]
                if not second and not first:
                    break
    return encrypted_text

print(encrypt("This is a test!", 0))
print(encrypt("This is a test!", 1))
print(encrypt("This is a test!", 2))
print(encrypt("This is a test!", -3))
print(encrypt("This kata is very interesting!", 1))

print(decrypt("This is a test!", 0))
print(decrypt("hsi  etTi sats!", 1))
print(decrypt("s eT ashi tist!", 2))
print(decrypt(" Tah itse sits!", 3))
print(decrypt("This is a test!", 4))
print(decrypt("This is a test!", -1))
print(decrypt("hskt svr neetn!Ti aai eyitrsig", 1))


"""
def decrypt(text, n):
    if text in ("", None):
        return text
    
    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i+1] + a[i:i+1] for i in range(ndx + 1))
    return text



def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text

"""