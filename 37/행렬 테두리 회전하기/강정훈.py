def solution(rows, columns, queries):
    answer = []
    arrays = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            arrays[i][j] = i * (columns) + (j + 1)
    for query in queries:
        x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        to_right_list = []
        to_down_list = []
        to_left_list = []
        to_up_list = []
        min_result = 9999999999999999
        for i in range(x1, x2):
            to_up_list.append((i+1, y1, arrays[i+1][y1]))
            to_down_list.append((i, y2, arrays[i][y2]))
            min_result = min(min_result, arrays[i+1][y1], arrays[i][y2])
        for j in range(y1, y2):
            to_right_list.append((x1, j, arrays[x1][j]))
            to_left_list.append((x2, j+1, arrays[x2][j+1]))
            min_result = min(min_result, arrays[x1][j], arrays[x2][j+1])
        answer.append(min_result)
        for to_left_info in to_left_list:
            arrays[to_left_info[0]][to_left_info[1] - 1] = to_left_info[2]
        for to_right_info in to_right_list:
            arrays[to_right_info[0]][to_right_info[1] + 1] = to_right_info[2]
        for to_up_info in to_up_list:
            arrays[to_up_info[0] - 1][to_up_info[1]] = to_up_info[2]
        for to_down_info in to_down_list:
            arrays[to_down_info[0] + 1][to_down_info[1]] = to_down_info[2]

        # 2,2,5,4 / 1,1,4,3
        # 2,2 ~ 2,3 to_right / 2,4 ~ 4,4 to_down / 5,3 ~ 5,4 to_left
        # / 2,1 ~ 4,1 to_up
    return arrays

rows1 = 100
columns1 = 97
queries1 = [[1,1,100,97]]
print(solution(rows1, columns1, queries1))