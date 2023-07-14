N = int(input())
S = input()

stack = []
answer = 0
rank = 0
for i in S:
    if not stack:
        stack.append(i)
        rank += 1
    
    elif i != stack[-1]:
        stack.pop()
        rank -= 1
    else:
        stack.append(i)
        rank += 1

    answer = max(rank, answer) 
if stack:
    answer = -1
print(answer)
