words = list(input())
target = list(input())
length = len(target)
answer = []
stack = []
idx = 0
for char in words:
    if char == target[idx]:
        idx += 1
    elif char == target[0]:
        stack.append(idx)
        idx = 1
    else:
        stack.append(idx)
        for num in stack:
            for i in range(num):
                answer.append(target[i])
        stack.clear()
        answer.append(char)
        idx = 0
    if idx == length:
        if stack:
            idx = stack.pop()
        else:
            idx = 0

stack.append(idx)
for num in stack:
    for i in range(num):
        answer.append(target[i])

if answer:
    print(''.join(answer))
else:
    print('FRULA')
'''
문자열 슬라이싱은 시간초과
리스트 stack pop이 통과
'''
# words = input()
# target = list(input())
# length = len(target)
# answer = []
# for i in words:
#     answer.append(i)
#     if answer[len(answer)-length:] == target:
#         for j in range(length):
#             answer.pop()
#
# if answer:
#     print(''.join(answer))
# else:
#     print('FRULA')