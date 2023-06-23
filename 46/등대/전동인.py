# 방법론.
# 1을 루트로 지정하고 root -> leaf로 DFS로 순회하면서 leaf -> root 순으로 뒤집어 담는다.
# leaf에서 부터 불을 킬 때와 안킬 때의 경우 수를 담는다.
# 이 때, dp[node][0]은 현재 노드에서 불 X, dp[node][1]은 현재노드에서 불 O

def solution(n, lighthouse):
    graph = [[] for _ in range(n+1)]
    dp = [[0, 0] for _ in range(n+1)]
    visited = [0] * (n+1)

    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)

    stack = [1]
    reverse = []
    visited[1] = 1

    # DFS - 단순 순회를 위한 로직
    while stack:
        node = stack.pop()
        reverse.append(node)
        for i in graph[node]:
            if not visited[i]:
                visited[i] = 1
                stack.append(i)
                graph[i].remove(node)  # 자식 노드에서 부모 노드로의 이동을 삭제

    # DP - stack에는 DFS의 역순이 저장되어 있고, leaf에서 부터 root(1)까지의 순서
    while reverse:
        node = reverse.pop()
        dp[node][1] = 1  # 불을 켠다
        for i in graph[node]:  # 자식의 dp를 가져옴
            # 현재 노드에서 불을 안 켰을 때 최소 등대의 개수, 내가 안켰기 때문에 자식은 항상 불을 켜야함.
            dp[node][0] += dp[i][1]
            # 현재 노드에서 불을 켰을 때 최소 등대의 개수, 내가 켰기 때문에 자식은 상관없음.
            dp[node][1] += min(dp[i])

    return min(dp[1])
