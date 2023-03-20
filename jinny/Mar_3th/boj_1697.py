# 숨바꼭질
from collections import deque
n, k = map(int, input().split())
if n != k:
    stack = deque()
    stack.append(n)
    end = k
    #bfs
    answer = 0
    visited = {stack[0]}
    while stack:
        for i in range(len(stack)):
            start = stack.popleft()
            if start + 1 == end or start - 1 == end or start * 2 == end:
                answer += 1
                stack = 0
                break
            for next in [start + 1, start - 1, start * 2]:
                if next not in visited and 0 <= next <= 100000:
                    stack.append(next)
                    visited.add(next)
            #
            # if start + 1 not in visited and start + 1 < 100000:
            #     stack.append(start + 1)
            #     visited.add(start + 1)
            # if start - 1 not in visited and start - 1 >= 0:
            #     stack.append(start - 1)
            #     visited.add(start - 1)
            # if start < end and start * 2 < 100000 and start * 2 not in visited:
            #     stack.append(start * 2)
            #     visited.add(start * 2)
        else:
            answer += 1
    print(answer)
else:
    print(0)