def dfs(n, money):
    if n == N:
        return True
    flag = False
    for door in maze[n][2]:
        if 1 < door <= N and door not in visited:
            visited.add(door)
            if maze[door][0] == 'L':
                flag = dfs(door, max(maze[door][1], money))
            elif maze[door][0] == 'T' and 0 <= money - maze[door][1]:
                flag = dfs(door, money - maze[door][1])
            elif maze[door][0] == 'E':
                flag = dfs(door, money)
            if flag:
                return True
            visited.remove(door)


while True:
    N = int(input())
    if N == 0:
        break
    maze = ['']
    for n in range(N):
        character, cost, *rooms, _ = input().split()
        maze.append((character, int(cost), tuple(map(int, rooms))))

    visited = set()
    if dfs(1, 0):
        print('Yes')
    else:
        print('No')
