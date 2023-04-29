def solution(n, k, cmd):

    # 각 인덱스마다 왼쪽, 오른쪽 인덱스를 가리키는 리스트
    left = [-1] + list(range(n))
    right = list(range(1, n)) + [-1]
    
    current = k
    deleted_stack = []
    deleted_set = set()
    
    for c in cmd:
        if c == "C":
            deleted_stack.append(current)
            deleted_set.add(current)
            right[left[current]], left[right[current]] = right[current], left[current]
            if right[current] != -1:
                current = right[current]
            else:
                current = left[current]
                                
        elif c == "Z":
            last_deleted = deleted_stack.pop()
            deleted_set.remove(last_deleted)
            right[left[last_deleted]], left[right[last_deleted]] = last_deleted, last_deleted
            
        elif c[0] == "U":
            jump = int(c.split()[1])
            for _ in range(jump):
                current = left[current]
                
        elif c[0] == "D":
            jump = int(c.split()[1])
            for _ in range(jump):
                current = right[current]
    
    answer = ""
    for idx in range(n):
        if idx in deleted_set:
            answer += "X"
        else:
            answer += "O"

    return answer