numb = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
date = ""
n = int(input())

for first in range(0, 3):
    for second in range(0, 10):
        if (first * 10 + second) < 24:
            for third in range(0, 7):
                for fourth in range(0, 10):
                    if (third * 10 + fourth) < 60:
                        if (numb[first] + numb[second] + numb[third] + numb[fourth]) == n:
                            date = str(first) + str(second) + ":" + str(third) + str(fourth)
if date == "":
    print("Impossible")
else:
    print(date)
