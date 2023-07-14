import sys
input = sys.stdin.readline

N = int(input())
S = input()
cnt = 1
stack = [S[0]]
for i in range(1, N):
    if not stack:
        stack.append(S[i])
    else:
        if S[i] == stack[-1]:
            stack.append(S[i])
        else:
            stack.pop()
    if len(stack) > cnt:
        cnt = len(stack)

if stack:
    print("-1")
else:
    print(cnt)
