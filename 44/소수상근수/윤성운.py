import sys
input = sys.stdin.readline

n = int(input())

memo = {1}
except_memo = set()

# 상근수 구하기
for num in range(1, n + 1):

    if num in memo or num in except_memo:
        continue

    tmp_memo = {num}
    initial = num
    while True:
        acc = 0
        for i in str(num):
            acc += int(i) ** 2

        # 사이클을 도는 경우 상근수 x
        if acc in tmp_memo:
            except_memo.update(tmp_memo)
            break
        tmp_memo.add(acc)

        # 상근수를 만난 경우
        if acc in memo:
            memo.update(tmp_memo)
            break
        # 상근수가 아닌 수를 만난 경우
        elif acc in except_memo:
            except_memo.update(tmp_memo)
            break
        num = acc

# 소수 구하기
prime_numbers = [0] * (n + 1)
for i in range(2, n + 1):
    if prime_numbers[i]:
        continue
    j = 2
    while i * j <= n:
        prime_numbers[i * j] = 1
        j += 1

# 소수상근수 구하기
for num in range(2, n + 1):
    if not prime_numbers[num] and num in memo:
        print(num)
