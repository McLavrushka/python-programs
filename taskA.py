n = int(input())
sumMin = None
for i in range(1, n + 1):
    a, b = map(int, input().split())
    sumOf = a + b
    if sumMin is None or sumOf < sumMin:
        sumMin = sumOf
print(sumMin)
