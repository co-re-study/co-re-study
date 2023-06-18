import sys
input = sys.stdin.readline

def comb(sidx, idx):
    global answer

    if sidx == cnt:
        selection_set = set(selection)
        acc = 0
        opposite_acc = 0

        # 고른 번호와 안 고른 번호 각각 누적값 구하기
        for i in range(N):
            for j in range(N):
                if i in selection_set and j in selection_set:
                    acc += arr[i][j]
                elif i not in selection_set and j not in selection_set:
                    opposite_acc += arr[i][j]
        
        if abs(acc - opposite_acc) < answer:
            answer = abs(acc - opposite_acc)
        return
    
    if idx == N:
        return
    
    selection[sidx] = idx
    comb(sidx + 1, idx + 1)
    comb(sidx, idx + 1)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total = 0
for i in range(N):
    total += sum(arr[i])
answer = 987654321

for cnt in range(1, N // 2 + 1):
    selection = [0] * cnt
    comb(0, 0)

print(answer)