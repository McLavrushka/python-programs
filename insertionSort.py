'''
Требуется отсортировать массив по неубыванию методом "вставок".

5 2 3 4 5
Входные данные
В первой строке вводится одно натуральное число, не превосходящее 1000 – размер массива.
Во второй строке задаются N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).

Выходные данные
Вывести получившийся массив
'''

N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    for j in range(i, 0, -1):
        if A[j - 1] > A[j]:
            A[j], A[j - 1] = A[j - 1], A[j]
        else:
            break
print(A)