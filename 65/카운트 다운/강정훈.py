def solution(target):
    INF = 1e9
    # 0번째 index는 target에 도달하는 최소 횟수, 1번째 index는 single 또는 bull의 최대 횟수
    answer = [0, 0]
    dp_table = [[INF, 0] for _ in range(target + 1)]
    dp_table[0] = [0, 0]
    single_bull_list, double_triple_list = create_table()
    for current_target_number in range(1, target + 1):
        for single_bull_number in single_bull_list:
            previous_value = current_target_number - single_bull_number

            if previous_value < 0:
                continue
            throwed_count, single_or_bull_count = dp_table[previous_value][0] + 1, dp_table[previous_value][1] + 1
            if throwed_count < dp_table[current_target_number][0]:
                dp_table[current_target_number] = [throwed_count, single_or_bull_count]

    # double_triple일 때 경우의수 넣어주기
    for current_target_number in range(1, target + 1):
        for double_triple_number in double_triple_list:
            previous_value = current_target_number - double_triple_number

            if previous_value < 0:
                continue
            throwed_count, single_or_bull_count = dp_table[previous_value][0] + 1, dp_table[previous_value][1]
            if throwed_count < dp_table[current_target_number][0]:
                dp_table[current_target_number] = [throwed_count, single_or_bull_count]
            elif throwed_count == dp_table[current_target_number][0]:
                dp_table[current_target_number] = [throwed_count,
                                                   max(single_or_bull_count, dp_table[current_target_number][1])]
    answer = dp_table[-1]

    return answer



# 싱글넘버와 bull 그룹, double, triple 그룹을 나눈 리스트를 반환해준다.
def create_table():
    single_bull_set, double_triple_set = set(), set()
    max_single_number = 20
    for single_number in range(1, max_single_number + 1):
        single_bull_set.add(single_number)
        double_number, triple_number = single_number * 2, single_number * 3
        if double_number > 20:
            double_triple_set.add(double_number)
        if triple_number > 20:
            double_triple_set.add(triple_number)
    bull_score = 50
    single_bull_set.add(bull_score)
    return list(single_bull_set), list(double_triple_set)
