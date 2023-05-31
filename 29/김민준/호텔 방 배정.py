from collections import defaultdict
#신청 순서대로 방 배정
# 투숙하기 원하는 방 번호 제출
# 고객이 원하는 방이 비어있다면 즉시 배정
# 고객이 원하는 방이 이미 배정되어 있으면 원하는 방보다
# 번호가 크면서 비어있는 방 중 가장 번호가 작은 방을 배정


# def solution(k, room_number):
#     answer = []
#     filled = defaultdict(int)
#     filled[0] = defaultdict(int)
#     #0이면 바로 찾고 그렇지 않으면 그 숫자 이상
#     #0인 것들 중에서 바로 팝하도록
#
#     #0인 것들 초기화
#     for i1 in range(1,k+1):
#         filled[0][i1] = 1
#
#     #방배정
#     for i2 in room_number:
#         if filled[i2] == 1 :
#             #0인 리스트에서 i2보다 큰 수를 탐색 후 그 리스트에서 최소값 추출
#             #리스트를 만든다 [i2+1,k]인
#             for i3 in range(i2+1,k+1):
#                 if filled[0][i3] == 1:
#                     filled[0][i3] = 0
#                     filled[i3] = 1
#                     answer.append(i3)
#                     break
#         else:
#             filled[i2] = 1
#             filled[0][i2] = 0
#             answer.append(i2)
#
#
#     return answer
def solution2(k, room_number):
    answer = []
    next_room_dict = defaultdict(int)
    for room in room_number:
        cur = room
        visit = {cur}
        while cur in next_room_dict:
            #다음방을 cur에 옮기자
            cur = next_room_dict[cur]
            #그리고 다음 방문할 visit에 cur를 넣자
            visit.add(cur)
        #다음 방이 없는 cur
        #이로써 visit이 완성되었고 이 visit에 있는 아이템을 하나씩 돌면서
        #다음방이 없는 cur을 해당 assign 뒤에
        for assign in visit:
            next_room_dict[assign] = cur+1
        answer.append(cur)
    return answer


k = 10
room_number = 	[1,3,4,1,3,1]
result = [1,3,4,2,5,6]
print(solution(k,room_number))


