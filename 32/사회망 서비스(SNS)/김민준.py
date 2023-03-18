import sys
sys.setrecursionlimit(10**7)
input =sys.stdin.readline
n = int(input())
tree_collection = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e = map(int,input().split())
    tree_collection[s].append(e)
    tree_collection[e].append(s)

visited = [False]*(n+1)

dp = [[0,1] for _ in range(n+1)]


def check(node):
    visited[node] = True
    for next in tree_collection[node]:
        if not visited[next]:
            #타고타고 가서 끝까지 가는 재귀 시작(dfs활용)
            check(next)
            # 얼리어답터가 아니면 다음 자손은 반드시 얼리어답터 이므로
            dp[node][0] += dp[next][1]
            # 얼리어답터인 경우에는 다음 자손이 얼리어답터의 유무는 상관이 없어서 다음 자손에서 누적된 얼리어답터 수 중 최소값을 누적
            dp[node][1] += min(dp[next][0],dp[next][1])
check(1)
#루트노드에서 얼리어답터 순의 최소값
print(min(dp[1][0],dp[1][1]))

## 디피 인줄도 몰랐음...
## 애초에 문제를 이해하는 것도 조금 쉽지 않았던듯 주위에 얼리어답터로 둘러쌓여야한다는거?
## 결국 정답을 보았지만 이해하는 것도 좀 걸렸다 ㅠ
