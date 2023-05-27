# 라이언이 이기는 모든 경우의 수 다 보기

def solution(n, info):
    max_diff = -1
    ans = [-1]

    def calc_score(score_list):
        nonlocal info
        apeach_score = lion_score = 0

        for idx in range(10):
            if info[idx] == score_list[idx] == 0:
                continue
            elif info[idx] < score_list[idx]:
                lion_score += 10 - idx
            elif info[idx] >= score_list[idx]:
                apeach_score += 10 - idx
        return (apeach_score, lion_score)

    def check_same_score(score_list):
        nonlocal ans

        for idx in range(10, -1, -1):
            if score_list[idx] > ans[idx]:
                return True
            elif score_list[idx] < ans[idx]:
                return False
        return False

    def play(idx=0, left_arrow=n, score_list=[0] * 11):
        nonlocal max_diff, ans

        if left_arrow == 0 or idx == 11:
            apeach_score, lion_score = calc_score(score_list)
            diff = lion_score - apeach_score
            if lion_score > apeach_score:
                if diff > max_diff or diff == max_diff and check_same_score(score_list):
                    max_diff, ans = diff, score_list[:]
            return
        else:
            play(idx + 1, left_arrow, score_list)
            score_list[idx] += 1
            if score_list[idx] == 1:
                play(idx, left_arrow - 1, score_list)
            else:
                play(idx, left_arrow - 1, score_list)
            score_list[idx] -= 1

    play()

    return ans


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))