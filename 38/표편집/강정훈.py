# 1차시도 정확성 테스트 100% // 효율성 테스트 모두 시간초과
def solution1(n, k, cmd):
    answer = ["O" for _ in range(n)]
    column_list = [i for i in range(n)]
    deleted_column_list = []
    current_index = k
    for command in cmd:
        if len(command) > 1:
            command = command.split()
            command, move = command[0], int(command[1])
        if command == "U":
            current_index -= move
        elif command == "D":
            current_index += move
        elif command == "C":
            deleted_column_list.append((current_index, column_list[current_index]))
            column_list.remove(column_list[current_index])
            if current_index == len(column_list):
                current_index -= 1
        elif command == "Z":
            restored_index, restored_value = deleted_column_list.pop()
            column_list.insert(restored_index, restored_value)
            if current_index >= restored_index:
                current_index += 1
    for X in deleted_column_list:
        answer[X[1]] = "X"
    answer = "".join(answer)

    return answer

# 2차시도 아슬아슬 통과
# 1차에서는 직접 리스트를 순회하면서 수정하는 형태로 구현했으나 시간초과가 났다.
# 시간초과가 나서 직접 돌면서 수정하는게 아니라 연결 상태를 기록하는 것이 필요하다고 생각해서,
# 각 인덱스마다 살아있는 인덱스 중 이전 인덱스와 이후 인덱스를 기록함.
def solution(n, k, cmd):
    answer = ["O" for _ in range(n)]
    column_list = [[i-1, i+1] for i in range(n)] # index마다 이전 행과 다음 행을 기록함.
    deleted_column_list = [] # 삭제된 index를 리스트[이전 index, 삭제된 index, 다음 index] 형태로 기록할 예정
    current_index = k
    for command in cmd:
        if len(command) > 1:
            command = command.split()
            command, move = command[0], int(command[1])
        if command == "U":
            for _ in range(move):
                current_index = column_list[current_index][0]
        elif command == "D":
            for _ in range(move):
                current_index = column_list[current_index][1]
        elif command == "C":
            pre_column, next_column = column_list[current_index][0], column_list[current_index][1]
            deleted_column_list.append((pre_column, current_index, next_column))
            answer[current_index] = "X"
            if next_column == n:
                column_list[pre_column][1] = next_column
                current_index = pre_column
            elif pre_column == -1:
                column_list[next_column][0] = pre_column
                current_index = next_column
            else:
                column_list[next_column][0] = pre_column
                column_list[pre_column][1] = next_column
                current_index = next_column
        elif command == "Z":
            pre_column, current_column, next_column = deleted_column_list.pop()
            if next_column == n:
                column_list[pre_column][1] = current_column
            elif pre_column == -1:
                column_list[next_column][0] = current_column
            else:
                column_list[pre_column][1] = current_column
                column_list[next_column][0] = current_column
            answer[current_column] = "O"
    answer = "".join(answer)



    return answer


n1 = 8
k1 = 2
cmd1 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n1, k1, cmd1))