# 빨강, 초록의 순서 및 빈 배양액 땅까지 고려하는 경우를 모두 구해야 함.

import sys
from itertools import combinations
from collections import deque
input=sys.stdin.readline
def BFS(green_start,red_start):
    GQ = deque([])
    RQ = deque([])
    flower=0
    cnt=1
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    for i in green_start:
        visited[i[0]][i[1]]=-2
        GQ.append(i)
    for i in red_start:
        visited[i[0]][i[1]]=-2
        RQ.append(i)
    while GQ and RQ:
        for _ in range(len(GQ)):
            rx,ry=GQ.popleft()
            if visited[rx][ry]==-100:
                continue
            for w in range(4):
                nrx=rx+dx[w]
                nry=ry+dy[w]
                if 0<=nrx<n and 0<=nry<m:
                    if adj[nrx][nry] and visited[nrx][nry]==-1:
                        visited[nrx][nry]=cnt
                        GQ.append((nrx,nry))

        for _ in range(len(RQ)):
            rx,ry=RQ.popleft()
            if visited[rx][ry]==-100:
                continue
            for w in range(4):
                nrx=rx+dx[w]
                nry=ry+dy[w]
                if 0<=nrx<n and 0<=nry<m:
                    if adj[nrx][nry]:
                        if visited[nrx][nry]==-1:
                            visited[nrx][nry]=-2
                            RQ.append((nrx,nry))
                        elif visited[nrx][nry]==cnt:
                            flower+=1
                            visited[nrx][nry]=-100
        cnt+=1
    return flower


n,m,g,r=map(int,input().split())
adj=[list(map(int,input().split()))for _ in range(n)]
max_flower=0
can_start=[]

for i in range(n):
    for j in range(m):
        if adj[i][j]==2:
            can_start.append((i,j))

for i in combinations(can_start,g+r):
    for green_start in combinations(i,g):
        visited = [[-1 for _ in range(m)] for _ in range(n)]
        red_start=[x for x in i if x not in green_start]
        temp=BFS(green_start,red_start)
        max_flower=max(max_flower,temp)

print(max_flower)