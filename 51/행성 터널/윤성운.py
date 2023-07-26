import sys
input = sys.stdin.readline

def find_parent(n):
    if n != parent[n]:
        parent[n] = find_parent(parent[n])
    return parent[n]


def union(n1, n2):
    n1 = find_parent(n1)
    n2 = find_parent(n2)
    if n1 == n2:
        return
    if n1 < n2:
        parent[n2] = n1
    else:
        parent[n1] = n2


def acc_answer(sorted_gap_list, idx):
    global answer
    # 부모가 다르면 union하고 정답 더하기
    if find_parent(sorted_gap_list[idx][1]) != find_parent(sorted_gap_list[idx][2]):
        union(sorted_gap_list[idx][1], sorted_gap_list[idx][2])
        answer += sorted_gap_list[idx][0]
    

N = int(input())
# ex) [[11, -15, -15], [14, -5, -15], [-1, -1, -5], [10, -4, -1], [19, -4, 19]]
planet_list = [list(map(int, input().split())) for _ in range(N)]

# x, y, z를 각각 정렬해서 관리
# [[좌표, 행성 번호]]
# ex) [[-1, 2], [10, 3], [11, 0], [14, 1], [19, 4]]
sorted_x_positions = sorted([[planet_list[i][0], i] for i in range(N)])
sorted_y_positions = sorted([[planet_list[i][1], i] for i in range(N)])
sorted_z_positions = sorted([[planet_list[i][2], i] for i in range(N)])

# gap순으로 정렬해서 관리
# [[차이, 행성1, 행성2]]
# ex) [[1, 3, 0], [3, 0, 1], [5, 1, 4], [11, 2, 3]]
sorted_x_gaps = sorted([[abs(sorted_x_positions[i + 1][0] - sorted_x_positions[i][0]), sorted_x_positions[i][1], sorted_x_positions[i + 1][1]] for i in range(N - 1)])
sorted_y_gaps = sorted([[abs(sorted_y_positions[i + 1][0] - sorted_y_positions[i][0]), sorted_y_positions[i][1], sorted_y_positions[i + 1][1]] for i in range(N - 1)])
sorted_z_gaps = sorted([[abs(sorted_z_positions[i + 1][0] - sorted_z_positions[i][0]), sorted_z_positions[i][1], sorted_z_positions[i + 1][1]] for i in range(N - 1)])

parent = list(range(N))
x_idx = 0
y_idx = 0
z_idx = 0
answer = 0

# 크루스칼 MST(x, y, z 중 가장 차이가 작은 것 찾아서 union)
while x_idx < N - 1 and y_idx < N - 1 and z_idx < N - 1:
    if sorted_x_gaps[x_idx][0] <= sorted_y_gaps[y_idx][0] and sorted_x_gaps[x_idx][0] <= sorted_z_gaps[z_idx][0]:
        acc_answer(sorted_x_gaps, x_idx)
        x_idx += 1

    elif sorted_y_gaps[y_idx][0] <= sorted_x_gaps[x_idx][0] and sorted_y_gaps[y_idx][0] <= sorted_z_gaps[z_idx][0]:
        acc_answer(sorted_y_gaps, y_idx)
        y_idx += 1

    elif sorted_z_gaps[z_idx][0] <= sorted_x_gaps[x_idx][0] and sorted_z_gaps[z_idx][0] <= sorted_z_gaps[z_idx][0]:
        acc_answer(sorted_z_gaps, z_idx)
        z_idx += 1

print(answer)