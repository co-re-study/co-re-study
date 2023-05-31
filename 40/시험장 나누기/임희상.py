def solution(k, num, links):
    answer = 0
    N = len(num)
    parents = [-1] * N
    children = [[] for _ in range(N)]
    leaves = set()

    for i in range(N):
        left, right = links[i]
        if left != -1:
            parents[left] = i
            children[i].append(left)
        if right != -1:
            parents[right] = i
            children[i].append(right)
        if left == -1 and right == -1:
            leaves.add(i)

    left = 0
    right = 10000 * N

    def is_possible(L):
        dp = [[0, 0] for _ in range(N)]
        stack = []
        for leaf in leaves:
            stack.append(leaf)
        visited = set()

        while stack:
            current = stack.pop()
            if num[current] > L:
                return False

            visited.add(current)

            if len(children[current]) == 2:
                target = min(dp[children[current][0]][0], dp[children[current][1]][0])
                if target + num[current] > L:
                    dp[current][0] = num[current]
                    dp[current][1] = dp[children[current][0]][1] + dp[children[current][1]][1] + 1
                else:
                    if sum([dp[children[current][0]][0], dp[children[current][1]][0]]) + num[current] > L:
                        dp[current][0] = num[current] + target
                        dp[current][1] = dp[children[current][0]][1] + dp[children[current][1]][1]
                    else:
                        dp[current][0] = sum([dp[children[current][0]][0], dp[children[current][1]][0]]) + num[current]
                        dp[current][1] = dp[children[current][0]][1] + dp[children[current][1]][1] - 1

            elif children[current]:
                target = dp[children[current][0]][0]
                if target + num[current] > L:
                    dp[current][0] = num[current]
                    dp[current][1] = dp[children[current][0]][1] + 1
                else:
                    dp[current][0] = num[current] + target
                    dp[current][1] = dp[children[current][0]][1]
            else:
                dp[current][0] = num[current]
                dp[current][1] = 1

            if dp[current][1] > k:
                return False
            if parents[current] == -1:
                return True
            for child in children[parents[current]]:
                if child not in visited:
                    break
            else:
                stack.append(parents[current])
                
    prev = 0
    mid = 0
    flag = False
    while left <= right:
        prev = mid
        mid = (right+left)//2
        if mid == prev:
            flag = True
        if is_possible(mid):
            right = mid
            if flag:
                break
        else:
            left = mid + 1

    return mid

