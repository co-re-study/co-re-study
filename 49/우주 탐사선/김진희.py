# 우주탐사선
def floyd_warshall():
    for k in range(n):  # i에서 j까지 갈 때 지나갈 수 있는 노드
        for i in range(n):
            for j in range(n):
                # 해당 노드를 경유하는 것이 더 짧은 거리가 된다면 갱신
                if arr[i][j] > arr[i][k] + arr[k][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]
    return


def space_probe(x, acc, visited):  # 현재 행성, 걸린 시간, 방문한 곳
    global answer

    for i in range(n):  # 현재 행성에서 갈 수 있는 곳을 모두 탐사
        if i != x:
            acc += arr[x][i]
            if len(visited | {i}) == n:  # 모든 행성을 방문했을 때,
                if acc < answer:         # 누적합이 최소라면
                    answer = acc         # 답을 갱신하고 종료
                return

            if i not in visited:
                space_probe(i, acc, visited | {i})
            acc -= arr[x][i]  # 다음 행성 확인하려면 누적합 되돌리기


n, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 99999
floyd_warshall()
space_probe(K, 0, {K})
print(answer)  # k번 행성에서 시작!
