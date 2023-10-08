'''
'.'는 빈 공간을 나타낸다.
'*'는 벽을 나타내며, 상근이는 벽을 통과할 수 없다.
'$'는 상근이가 훔쳐야하는 문서이다.
알파벳 대문자는 문을 나타낸다.
알파벳 소문자는 열쇠를 나타내며, 그 문자의 대문자인 모든 문을 열 수 있다.
'''
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    docu = ['.'*(w+2)]+[['.']+list(input())+['.']
                        for _ in range(h)]+['.'*(w+2)]
    keys = set(input())
    visited = [[0]*(w+2) for _ in range(h+2)]
    visited_docu = []
    queue = deque([[0, 0]])
    visited[0][0] = 1
    ans = 0
    while queue:
        x0, y0 = queue.popleft()
        for i in range(4):
            x1 = x0+dx[i]
            y1 = y0+dy[i]
            if 0 > x1 or x1 >= h+2 or 0 > y1 or y1 >= w+2 or visited[x1][y1] or docu[x1][y1] == '*':
                continue
            if 'A' <= docu[x1][y1] <= 'Z':
                if chr(ord(docu[x1][y1])+32) not in keys:
                    continue
            if 'a' <= docu[x1][y1] <= 'z':
                if docu[x1][y1] not in keys:
                    keys.add(docu[x1][y1])
                    visited = [[0]*(w+2) for _ in range(h+2)]
            if docu[x1][y1] == '$' and (x1, y1) not in visited_docu:
                ans += 1
                visited_docu.append((x1, y1))
            visited[x1][y1] = 1
            queue.append([x1, y1])
    print(ans)