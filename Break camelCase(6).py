"""
Завершите решение, чтобы функция разбивала верблюжий регистр, используя пробелы между словами.

Пример
"верблюжья оболочка" => "верблюжья оболочка"
"идентификатор" => "идентификатор"
"" => ""

"""


def solution(s: str):
    return "".join([' ' + char if char.isupper() else char for char in s])


print(solution("helloWorld"))
print(solution("camelCase"))
print(solution("breakCamelCase"))