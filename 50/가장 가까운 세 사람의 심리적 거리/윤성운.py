import sys
input = sys.stdin.readline

# 최악의 경우: 48C3
def comb(sidx, idx):
    global answer

    if sidx == 3:
        acc = 0
        for i in range(4):
            if selection[0][i] != selection[1][i]:
                acc += 1
            if selection[1][i] != selection[2][i]:
                acc += 1
            if selection[2][i] != selection[0][i]:
                acc += 1
        answer = min(answer, acc)
        return
    
    if idx == len(people):
        return
    
    selection[sidx] = people[idx]
    comb(sidx + 1, idx + 1)
    comb(sidx, idx + 1)

T = int(input())
for _ in range(T):
    N = int(input())
    mbti_list = list(input().split())
    mbti_cnt_dict = dict()
    people = []

    # 최대 3개만 people 리스트에 저장
    for current_mbti in mbti_list:
        if current_mbti in mbti_cnt_dict:
            if mbti_cnt_dict[current_mbti] == 3:
                continue
            mbti_cnt_dict[current_mbti] += 1
        else:
            mbti_cnt_dict[current_mbti] = 1
        people.append(current_mbti)

    selection = [0] * 3
    answer = 987654321
    comb(0, 0)

    print(answer)
    
