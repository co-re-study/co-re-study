# 숫자 연결하기
n, k = map(int, input().split())
answer = 1  # 이어진 횟수
num = n     # 나눌 수
remainder = set()
while True:
    if not num % k:
        print(answer)
        break
    else:
        # 나머지가 또 나오면 -1
        if num % k in remainder:
            print(-1)
            break
        remainder.add(num % k)

        num = int(str(num % k) + str(n))
        answer += 1