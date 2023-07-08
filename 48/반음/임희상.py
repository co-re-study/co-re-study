piano = ["A", 0, "B", "C", 0, "D", 0, "E", "F", 0, "G", 0]
answer = []

n = int(input())
moves = []
for _ in range(n):
    moves.append(int(input()))

for start in [0, 2, 3, 5, 7, 8, 10]:
    current = start
    for move in moves:
        current += move + 12
        current %= 12

        if not piano[current]:
            break
    else:
        answer.append(piano[start] + ' ' + piano[current])

for target in answer:
    print(target)

