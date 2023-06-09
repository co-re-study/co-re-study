from collections import deque


def solution(sales, links):
    # 트리 dp
    # 리프부터 쌓아 올려갈 것
    # 쌓아 올릴 값은 최소 매출액
    # 어떤 노드가 큐에서 나오면 해당 노드의 모든 자식들의 최솟값을 알고 있다.
    # [나를 선택했을 경우 최솟값, 선택하지 않았을 경우 최솟값]을 저장하고
    # 부모노드의 모든 자식들에 대해 위의 값들을 알게되면 부모노드를 큐에 넣어줌
    # 1번노드까지 수행하면 끝
    answer = 0
    parents = [0] * (len(sales) + 1)
    children = [set() for _ in range(len(sales) + 1)]
    children_clone = [set() for _ in range(len(sales) + 1)]
    for link in links:
        parent, child = link
        parents[child] = parent
        children[parent].add(child)
        children_clone[parent].add(child)
    dp = [[0, 0] for _ in range(len(sales) + 1)]
    # [내가 갈때, 내가 안갈때]
    queue = deque([])
    for node in range(1, len(sales) + 1):
        if not children[node]:
            queue.append(node)
    while queue:
        current = queue.popleft()
        dp_1 = 0  # 내가 워크샵을 감
        dp_2 = 0  # 내가 안갈 때 들어감
        if children[current]:
            children_dp = []
            min_diff = float('inf')
            for child in children[current]:  # 어쩔수 없이 워크샵을 가야하는 녀석 찾기
                children_dp.append(dp[child])
                if dp[child][0] - dp[child][1] < min_diff:
                    # [0]은 내가 갈 경우, [1]은 안갈 경우
                    # 두 값을 비교해서 가장 이득이 되는 녀석
                    min_diff = dp[child][0] - dp[child][1]
            flag = False  # 팀에 워크샵을 가는 사람이 있는지 확인
            for child in children_dp:
                dp_1 += min(child)  # current가 워크샵을 가니 그 자식은 가건 안가건 중요하지 않음
                if child[0] - child[1] == min_diff:
                    if flag:  # 이미 누군가 워크샵을 떠남
                        dp_2 += min(child)
                    else:  # 아무도 없으니 이녀석이 감
                        dp_2 += child[0]
                        flag = True
                    continue
                dp_2 += min(child)
                if min(child) == child[0]:
                    falg = True
        dp[current] = [dp_1 + sales[current - 1], dp_2]
        children_clone[parents[current]].discard(current)
        if not children_clone[parents[current]]:
            queue.append(parents[current])
        if current == 1:
            break
    answer = min(dp[1])

    return answer