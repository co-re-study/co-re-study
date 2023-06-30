import sys, math
input = sys.stdin.readline

# 순열
def perm(depth):
    global answer

    if depth == N:
        if tuple(selection) in visited:
            return
        acc = 0
        cnt = 0
        under_fifty_nums = set()
        for num in selection:
            acc += num
            if acc < 50: # 50보다 낮은 숫자 저장
                under_fifty_nums.add(acc)
            elif acc == 50: # 50이면 무조건 선 하나 생성
                cnt += 1
            else: # 50보다 크면 선으로 이어지는지 확인
                if acc - 50 in under_fifty_nums:
                    cnt += 1
        if cnt > answer:
            answer = cnt
        return
    
    for i in range(N):
        if not check[i]:
            check[i] = 1
            selection[depth] = dogs[i]
            perm(depth + 1)
            check[i] = 0

N = int(input())
dogs = list(map(int, input().split()))

check = [0] * N
selection = [0] * N
visited = set()
answer = 0

perm(0)

print(answer)