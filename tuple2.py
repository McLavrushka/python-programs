'''
Функция slicer() на вход принимает кортеж и случайный элемент.
Требуется вернуть новый кортеж, начинающийся с первого появления элемента в нем и заканчивающийся вторым его появлением включительно.
Если элемента нет вовсе – вернуть пустой кортеж.
Если элемент встречается только один раз, то вернуть кортеж, который начинается с него и идет до конца исходного.
'''

B = ()
minCount = 0
maxCount = -1


def slicer(tpl, rand):
    first = second = minCount
    if rand in tpl:
        first = tpl.index(rand)
        if tpl.count(rand) > 1:
            second = tpl.index(rand, first + 1) + 1
        else:
            second = len(tpl) + 1
    return tpl[first:second]


print(slicer((3, 4, 6, 3, 5, 3, 8), 3))
print(slicer((3, 4, 6, 3, 5, 3, 8), 4))
print(slicer((3, 4, 6, 3, 5, 3, 8), 44))
