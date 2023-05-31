def solution(n, info):
    
    def find_answer(idx, my_score, oppo_score, remain, memo):
        nonlocal answer, max_gap
        
        # 화살을 다 쏜 경우
        if idx == 11:
            # 남은 화살은 모두 0점으로 처리
            if remain:
                memo[-1] = remain
            if my_score > oppo_score:
                # 점수 차이가 최대인 경우 정답 갱신
                if my_score - oppo_score > max_gap:
                    max_gap = my_score - oppo_score
                    answer = memo[:]
                # 점수 차이가 같은 경우 더 낮은 점수를 많이 맞힌 경우를 정답으로
                elif my_score - oppo_score == max_gap:
                    for i in range(10, -1, -1):
                        if answer[i] > memo[i]:
                            break
                        elif answer[i] < memo[i]:
                            answer = memo[:]
                            break
            return
        
        # 상대 점수가 있는 경우 점수 내주기
        if info[idx]:
            find_answer(idx+1, my_score, oppo_score + 10 - idx, remain, memo + [0])
        # 상대 점수가 없으면 둘 다 점수 x
        else:
            find_answer(idx+1, my_score, oppo_score, remain, memo + [0])
        # 현재 과녁에서 상대보다 많이 맞힐 수 있으면 점수 가져가기
        if info[idx] < remain:
            find_answer(idx+1, my_score + 10 - idx, oppo_score, remain - info[idx] - 1, memo + [info[idx] + 1])
            
    answer = [-1]
    max_gap = -1
    find_answer(0, 0, 0, n, [])
    return answer