'''
Требуется отсортировать массив по неубыванию методом "выбор максимума".

42351

Входные данные
В первой строке вводится одно натуральное число, не превосходящее 1000 – размер массива.
Во второй строке задаются N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).
'''

N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    maxN = A[i]
    maxIndex = i
    for j in range(i + 1, N):
        if maxN < A[j]:
            maxN = A[j]
            maxIndex = j
    if i != maxIndex:
        A[i], A[maxIndex] = A[maxIndex], A[i]

print(A)
