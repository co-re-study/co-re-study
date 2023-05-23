'''
이분탐색을 해야하는데 어떤 걸 이분탐색할건지 생각해보자.
거리로 할지, 지점으로 할지.
생각해보니까 거리로 하는게 맞는거 같음.
왜냐하면 지점으로 하면 그 지점에 없을수도 있고,
탐색을 더 오래 진행해야 할 것 같음.
거리로 한다면, 최소 1, 최대 끝지점-시작지점이 된다.
있는 지점 모두 탐색해보면서 공유기를 설치해본다.
그런데 count가 더 많다는건 더 넓게 깔아도 된다는 거니까
최소인 s를 m+1로 놓고 다시 이분탐색해보기.
그 반대라면 더 설치를 해야하니까 e를 m-1로 이분탐색한다.
'''


import sys
input = sys.stdin.readline
N, C = map(int, input().split())
routers = sorted([int(input()) for _ in range(N)])
s, e = 1, routers[-1]-routers[0]
ans = 0
while s <= e:
    m = (s+e)//2
    curr = routers[0]
    count = 1
    for i in range(1, N):
        if routers[i] >= curr+m:
            count += 1
            curr = routers[i]
    if count >= C: # 더 많이 설치된다는 건 더 넓게 깔아도 된다는 것.
        s = m+1
        ans = m # 어차피 갱신되면 계속 큰 값으로 갱신됨
    else:
        e = m-1
print(ans)