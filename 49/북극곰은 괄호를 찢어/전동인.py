n = int(input())
s = input()

stack = []
day = 0

for i in range(n):
    # () => pop
    if s[i] == '(' and stack and stack[-1] == ')':
        stack.pop()

    # ( => push
    elif s[i] == '(':
        stack.append(s[i])

    # )( => pop
    elif s[i] == ')' and stack and stack[-1] == '(':
        stack.pop()

    # ) => push
    elif s[i] == ')':
        stack.append(s[i])

    day = max(len(stack), day)

# 원하는 문자열을 만들지 못했다면
if stack:
    print(-1)
else:
    print(day)
