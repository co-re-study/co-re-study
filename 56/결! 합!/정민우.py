from itertools import combinations

board = [list(input().split()) for _ in range(9)]
answers = set()
for a, b, c in combinations(range(9), 3):
    count = 0
    for i in range(3):
        check = len({board[a][i], board[b][i], board[c][i]})
        if check == 1 or check == 3:
            count += 1
    if count == 3:
        answers.add((a + 1, b + 1, c + 1))

g_count = False
point = 0
for _ in range(int(input())):
    command = input().split()
    if command[0] == 'H':
        _, a, b, c = command
        numbers = tuple(sorted(map(int, [a, b, c])))
        if numbers in answers:
            answers.remove(numbers)
            point += 1
        else:
            point -= 1
    else:
        if not answers and not g_count:
            point += 3
            g_count = True
        else:
            point -= 1

print(point)