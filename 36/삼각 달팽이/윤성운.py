def solution(n):
    answer = [0] * (n * (n + 1) // 2)
    answer[0] = 1
    idx = 0
    jump = 1
    current = 1
    
    while current < n * (n + 1) // 2:
        
        # 맨 왼쪽에서 밑으로 이동하면서 숫자 채우기
        while idx + jump < len(answer) and not answer[idx + jump]:
            idx += jump
            current += 1
            answer[idx] = current
            jump += 1
            
        # 오른쪽으로 이동하면서 숫자 채우기
        while idx + 1 < len(answer) and not answer[idx + 1]:
            idx += 1
            current += 1
            answer[idx] = current
            
        # 오른쪽 끝에서 위로 올라가면서 숫자 채우기
        while idx - jump >= 0 and not answer[idx - jump]:
            idx -= jump
            current += 1
            answer[idx] = current
            jump -= 1
            
    return answer