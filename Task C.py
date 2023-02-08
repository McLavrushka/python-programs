s = str(input())
t = str(input())
t = list(t)
print(t)
A = []
count = 0
n = 0
for i in range(0, len(t)):
    for k in range(0,len(t)):
        if t[i:k] not in A:
            print(i,k)
            print(t[i:k])
            A.append(t[i:])
            count += 1

for i in range(0, len(s)):
    for k in range(0,len(s)):
        under_s = s[i:k]
        if under_s in A:
            n += 1
print(n)


