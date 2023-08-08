# 모든 CCTV의 방향을 90도씩 돌려가면서 백트래킹

cctv_dir = [0, 
        [[(-1, 0)], [(0, 1)], [(1, 0)], [(0, -1)]], 
        [[(-1, 0), (1, 0)], [(0, 1), (0, -1)]], 
        [[(-1, 0), (0, 1)], [(-1, 0), (0, -1)], [(1, 0), (0, -1)], [(0, 1), (1, 0)]], 
        [[(-1, 0), (0, 1), (1, 0)], [(-1, 0), (0, 1), (0, -1)], [(-1, 0), (1, 0), (0, -1)], [(0, 1), (1, 0), (0, -1)]], 
        [[(-1, 0), (0, 1), (1, 0), (0, -1)]]]

N, M = map(int, input().split())
blind = set()
wall = set()
cctv = []
for n in range(N):
    row = list(map(int, input().split()))
    for m in range(M):
        if row[m] == 0:
            blind.add((n, m))
        elif row[m] == 6:
            wall.add((n, m))
        else:
            cctv.append((row[m], (n, m)))

def solution(visited, sight, depth):
    global ans
    if depth == len(cctv):
        if len(blind) - sight < ans:
            ans = len(blind) - sight
        return
    
    d, now = cctv[depth]
    for angle in cctv_dir[d]:
        now_sight, now_visited = 0, set()
        for di, dj in angle:
            ni, nj = now[0] + di, now[1] + dj
            while 0 <= ni < N and 0 <= nj < M and (ni, nj) not in wall:
                if (ni, nj) in blind and (ni, nj) not in visited and (ni, nj) not in now_visited:
                    now_sight += 1
                    now_visited.add((ni, nj))
                ni, nj = ni + di, nj + dj

        solution(visited | now_visited, sight + now_sight, depth + 1)

ans = 9999999999
solution(set(), 0, 0)

print(ans)