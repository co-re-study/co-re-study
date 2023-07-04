import sys
input = sys.stdin.readline

n = int(input())
moves = []
for _ in range(n):
    moves.append(int(input()))

# 피아노 건반 리스트 생성
piano = ["A", 0, "B", "C", 0, "D", 0, "E", "F", 0, "G", 0]
answer = []

# 완탐
for start in [0, 2, 3, 5, 7, 8, 10]:
    idx = start
    for move in moves:
        if move >= 0:
            for i in range(move):
                idx += 1
                if idx == 12:
                    idx = 0
        else:
            for i in range(abs(move)):
                idx -= 1
                if idx == -1:
                    idx = 11

        # 검은 건반을 누르면 break
        if not piano[idx]:
            break
    # 모두 흰 건반을 눌렀을 때만 정답 추가
    else:
        answer.append(f"{piano[start]} {piano[idx]}")

for i in answer:
    print(i)