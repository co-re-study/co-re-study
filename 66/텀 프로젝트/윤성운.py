import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def update_team(start, current, preferences, visited):
    visited[current] = 1
    if start == current:
        return
    update_team(start, preferences[current], preferences, visited)


def update_solo(path_set, visited):
    for i in path_set:
        if not visited[i]:
            visited[i] = 2


def is_team_possible(current, path_set, preferences, visited):
    if visited[current]:
        update_solo(path_set, visited)
        return
    if current not in path_set:
        path_set.add(current)
    else:
        update_team(current, preferences[current], preferences, visited)
        update_solo(path_set, visited)
        return
    is_team_possible(preferences[current], path_set, preferences, visited)
        

def find_solo_cnt(n, preferences):
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            is_team_possible(i, set(), preferences, visited)
    return sum(map(lambda x: 1 if x == 2 else 0, visited))


T = int(input())
for _ in range(T):
    n = int(input().strip())
    preferences = list(map(lambda x: int(x) - 1, input().strip().split()))
    print(find_solo_cnt(n, preferences))