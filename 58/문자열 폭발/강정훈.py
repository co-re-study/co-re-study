import sys
input=sys.stdin.readline
S = input().rstrip()
bomb = list(input().rstrip())

answer = []
idx = 0
for i in range(len(S)):
    answer.append(S[i])

    if len(answer) >= len(bomb) and answer[-1] == bomb[-1]:
        if answer[idx-len(bomb)+1:] == bomb[:]:
            for j in range(len(bomb)):
                answer.pop()
            idx -= len(bomb)
    idx += 1
if answer:
    print("".join(answer))
else:
    print("FRULA")


