import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    parent = [[] for _ in range(N + 1)]
    children = [[] for _ in range(N + 1)]
    parent_cnt = [0] * (N + 1)

    for _ in range(K):
        n1, n2 = map(int, input().split())
        parent[n2].append(n1)
        children[n1].append(n2)
        parent_cnt[n2] += 1

    # 부모 노드가 없는 노드만 stack에 저장
    stack = []
    for i in range(1, N + 1):
        if not parent[i]:
            stack.append(i)

    # 내 부모 노드 중 가장 누적된 시간이 많은 시간 저장
    max_parent_times = [0] * (N + 1)
    W = int(input())
    while stack:
        current = stack.pop()
        if current == W:
            break
        for dest in children[current]:
            # 자식 노드의 부모 중 현재 노드가 가장 많은 시간을 누적했다면 갱신
            max_parent_times[dest] = max(max_parent_times[dest], times[current] + max_parent_times[current])
            parent_cnt[dest] -= 1
            if not parent_cnt[dest]:
                stack.append(dest)

    print(max_parent_times[W] + times[W])
    
