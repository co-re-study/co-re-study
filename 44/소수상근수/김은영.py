# 소수 이면서 상근 수 여야 한다.
# 무한 루프에 빠지지 않게 주의해야 한다.
# 소수를 그냥 구하면 시간초과
# 에라토스테네스의 체를 쓰면 통과

def solution(number):
    num = number
    visit = set()
    while True:
        temp = 0
        while num > 0:
            temp += (num % 10) ** 2
            num //= 10
        if temp in visit:
            break
        if temp == 1:
            visit.add(1)
            answer.append(number)
            break
        visit.add(temp)
        num = temp


n = int(input())

so_number = [False, False] + [True] * (n-1)
for i in range(2, n + 1):
    if so_number[i]:
        for j in range(2*i, n+1, i):
            so_number[j] = False

answer = []

for i in range(2, n+1):
    solution(i)

for i in answer:
    if so_number[i]:
        print(i)
