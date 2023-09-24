origin = list(input())
target = list(input())

stack = []

for i in origin:
    stack.append(i)

    if stack[-len(target):] == target:
        for _ in range(len(target)):
            stack.pop()
    
if stack:
    print(''.join(stack))
else:
    print('FRULA')
