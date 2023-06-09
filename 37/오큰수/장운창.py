N = int(input())
line = list(map(int,input().split()))[::-1]
box = []
stack = []
for i in line:
    while stack and stack[-1] < i:
        stack.pop()
    if not stack:
        stack.append(i)
    if stack[-1] > i:
        box.append(stack[-1])
        stack.append(i)
    elif stack[-1] == i:
        if len(stack) == 1:
            box.append(-1)
        else:
            box.append(stack[-2])
print(*box[::-1])
'''
! input !
20
5 4 6 9 8 41 3 2 1 5 4 7 5 52 4 5 5 4 5 45
! output !
6 6 9 41 41 52 5 5 5 7 7 52 52 -1 5 45 45 5 45 -1
! script stack !
45 // 45 -1
45 5 // 5 45
45 5 // 4 5
45 5 // 5 45
45 5 // 5 45
45 5 // 4 5
52 // 52 -1
52 5 // 5 52
52 7 // 7 52
52 7 4 // 4 7
52 7 5 // 5 7
52 7 5 // 1 5
52 7 5 // 2 5
52 7 5 // 3 5
52 41 // 41 52
52 41 8 // 8 41
52 41 9 // 9 41
52 41 9 6 // 6 9
52 41 9 6 4 // 4 6
52 41 9 6 5 // 5 6
'''