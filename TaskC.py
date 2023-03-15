s = str(input())
t = str(input())
t = list(t)
s = list(s)
A = []
C = []
count = 0
n = 0
for i in range(0, len(t) + 1):
    for k in range(i, len(t) + 1):
        if t[i:k] not in A:
            A.append(t[i:k])
            count += 1
B = A[1:]
print(B)

for a in range(0, len(s) + 1):
    for b in range(a, len(s) + 1):
        underS = s[a:b]
        for k in range(len(underS)):
            C.append(underS[k])
        if underS in B or C in B:
            n += 1
            print(underS)
print(n)
