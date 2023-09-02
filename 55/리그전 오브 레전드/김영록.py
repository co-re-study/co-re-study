import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
arr = list(map(int, input().split()))
team = [0, arr[0]]+[0]*(N-1)
league = [0]*(N+1)
for i in range(2, N+1):
    team[i] = team[i-1]+arr[i-1]
    league[i] = league[i-1]+arr[i-1]*team[i-1]
for _ in range(Q):
    l, r = map(int, input().split())
    print(league[r]-league[l-1]-team[l-1]*(team[r]-team[l-1]))
