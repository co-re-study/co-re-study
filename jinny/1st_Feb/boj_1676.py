# 팩토리얼 0의 개수
n = int(input())
num = 1
for i in range(2, n + 1):
    num *= i
answer = 0
for i in str(num)[::-1]:
    if i == '0':
        answer += 1
    else:
        break
print(answer)