import sys
input = sys.stdin.readline

M, N = map(int, input().split())

left_and_top = [1] * (2*M-1)

for _ in range(N):
    zeros, ones, twos = map(int, input().split())

    for i in range(zeros, zeros+ones):
        left_and_top[i] += 1
    
    for i in range(zeros + ones, 2*M-1):
        left_and_top[i] += 2

answer = []
for i in range(M):
    for j in range(M):
        if j:
            answer.append(str(left_and_top[M+j-1])+' ')
        else:
            answer.append(str(left_and_top[M-i-1])+' ')
    answer.append('\n')

print(''.join(answer))
