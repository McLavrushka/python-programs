'''
Перед студентом стоит задача: на вход функции sieve() поступает список целых чисел.
В результате выполнения этой функции будет получен кортеж уникальных элементов списка в обратном порядке
'''

A = ()


def sieve(list_of_numbers):
    A = []
    for numb in reversed(list_of_numbers):
        if numb not in A:
            A.append(numb)
    return tuple(A)


print(sieve((3, 5, 6, 2, 1, 8, 4, 11, 2, 1)))
