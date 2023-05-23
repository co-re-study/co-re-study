N, C = map(int, input().split())

arr = []
for _ in range(N):
    a = int(input())
    arr.append(a)

arr.sort()
len_arr = len(arr)
distMin = 1
distMax = (arr[-1] - arr[0]) // (C-1)

rst = 1
while distMin  < distMax:
    if (distMax+distMin)%2 == 1:
        mid = (distMax + distMin)//2 + 1
    else:
        mid = (distMax + distMin)//2
    cnt = 1
    homes = [arr[0]]
    for i in range(1, len_arr): # 배열을 돌면서
        if cnt == C:
            break
        if (arr[i] - homes[-1]) >= mid: # 전 집과의 거리가 mid보다 크거나 같으면 
            homes.append(arr[i])      # 설치함
            cnt += 1
        else:
            pass

    if cnt == C:
        distMin = mid
        rst = mid
    elif distMax - distMin == 1:
        break
    else:
        distMax = mid

print(rst)





# 재귀 시간 초과 

# import sys
# sys.setrecursionlimit(10**6)


# def solution(house_list, point, cnt, diff):
#     global C, dist, len_arr, flag
#     if len(house_list) > C:
#         return
#     # print(cnt, house_list, diff)

    
    
#     if cnt == C:
#         dist = max(dist, diff)
#         flag = False
#         return
#     a = diff
#     for i in range(point, len_arr):
#         house_list.append(arr[i])
#         if len(house_list) >= 2:
#             temp_diff = abs(house_list[-1] - house_list[-2])
#             if temp_diff <= dist:
#                 continue
#             if temp_diff > diff:
#                 pass
#             elif temp_diff <= diff:
#                 diff = temp_diff
                
#         solution(house_list, i+1, cnt+1, diff)
#         diff = a
#         house_list.pop()
#         if not flag:
#             break
#     flag = True

# N, C = map(int, input().split())

# arr = []
# for _ in range(N):
#     a = int(input())
#     arr.append(a)

# arr.sort()
# len_arr = len(arr)
# dist = 0
# flag = True
# solution([], 0, 0, 987654321 )

# print(dist)

