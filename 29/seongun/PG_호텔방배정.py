import sys
sys.setrecursionlimit(100000)

def solution(k, room_number):
    
    def find_parent(num):
        # parent에 없다면 현재 숫자 return
        if num not in parent_dict:
            return num
        
        if parent_dict[num] != num:
            parent_dict[num] = find_parent(parent_dict[num])
            return find_parent(parent_dict[num])
        return num
    
    answer = []
    parent_dict = dict()
    for num in room_number:
        # 숫자가 parent에 있으면 빈 방 찾아서 배정
        if num in parent_dict:
            next_num = find_parent(num)
            parent_dict[next_num] = next_num + 1
            answer.append(next_num)
 
        # 숫자가 parent에 없으면 현재 방으로 배정
        else:
            parent_dict[num] = num + 1
            answer.append(num)
            
    return answer