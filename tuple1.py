'''
Напишите функцию tpl_sort(), которая сортирует кортеж, состоящий из целых чисел по возрастанию и возвращает его.
Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж.
'''


# A = (1, 4, 2, 7, 5)
# N = len(A)
# B = []*N
#
# print(B)
# def tpl_sort(A):
#     for i in range(N - 1):
#         if i % 1 == 0:
#             for j in range(N - i - 1):
#                 if j % 1 == 0:
#                     if A[i] > A[j]:
#                         B[i], B[j] = A[j], A[i]
#                 else:
#                     break
#         else:
#             break
#     return A
#
# tpl_sort(A)

def tpl_sort(tpl):
    for element in tpl:
        if not isinstance(element, int):
            return tpl
    return tuple(sorted(tpl))


# Тесты
print(tpl_sort((5, 5, 3, 1, 9)))
print(tpl_sort((5, 5, 2.1, '1', 9)))
