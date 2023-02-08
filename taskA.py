print("Input value")
n = int(input(""))
min = 10**9
for i in range(1, n+1):
    a,b=map(int,input().split())
    sum = a + b
    if sum < min:
        min = sum
print(min)