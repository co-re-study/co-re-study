from math import comb
n = int(input())
answer = 0
for i in range(1, 14):
    if n >= 4*i:
        if i % 2:
            answer = (answer + comb(52 - 4 * i, n - 4 * i) * comb(13, i)) % 10007
        else:
            answer = (answer - comb(52 - 4 * i, n - 4 * i) * comb(13, i)) % 10007
print(answer)