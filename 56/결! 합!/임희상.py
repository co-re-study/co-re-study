from itertools import combinations

board = []

for _ in range(9):
    board.append(input().split())

h_set = set()

for a, b, c in combinations(range(9), 3):
    for i in range(3):

        if board[a][i] != board[b][i] and board[b][i] != board[c][i] and board[c][i] != board[a][i]:
            continue
        if board[a][i] == board[b][i] == board[c][i]:
            continue
        break
    
    else:
        h_set.add((a, b, c))

n = int(input())
answer = 0

for i in range(1, n+1):
    claim= input().split()

    if claim[0] == 'G':
        if not h_set:
            answer += 3 - (n-i)
            break
        answer -= 1    
    else:
        a, b, c = map(lambda x: int(x)-1, claim[1:])
        try:
            h_set.remove(tuple(sorted([a, b, c])))
            answer += 1
        except:
            answer -= 1

print(answer)
exit(0)
    
