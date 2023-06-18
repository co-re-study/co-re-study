N = int(input())
board = []

answer = 0
for _ in range(N):
    board.append(list(map(int, input().split())))
    answer += sum(board[-1])

full = (1<<N) - 1

for i in range(1<<N):
    j = full - i
    target = set()
    other = set()

    for k in range(N):
        if i & 1<<k:
            target.add(k)
        else:
            other.add(k)
    team1 = 0
    team2 = 0
    for member1 in target:
        for member2 in target:
            team1 += board[member1][member2]
    for member1 in other:
        for member2 in other:
            team2 += board[member1][member2]

    answer = min(answer, abs(team1-team2))

print(answer)
