N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

for middle in range(N):
    for i in range(N):
        for j in range(N):
            matrix[i][j] = min(matrix[i][j], matrix[i][middle] + matrix[middle][j])

def find_ans(start=K, t=0, depth=1):
    global ans

    if depth == N:
        ans = min(t, ans)
        return
    
    for end in range(N):
        if end not in visited and t + matrix[start][end] < ans:
            visited.add(end)
            find_ans(end, t + matrix[start][end], depth + 1)
            visited.remove(end)
        
visited, ans = {K}, 9999999999
find_ans()
print(ans)