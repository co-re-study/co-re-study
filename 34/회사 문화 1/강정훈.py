from collections import deque

# 1차 시도 15%인가 17%에서 시간초과
# 사람수, 최초칭찬회수 = map(int, input().split())
# 직장상사리스트 = [0] + list(map(int, input().split())) # -1은 상사가 없다는 것을 의미 -> 사장임
#
# 칭찬력리스트 = [0 for _ in range(사람수+1)]
# 직속부하딕셔너리 = dict()
# for i in range(1, 사람수+1):
#     if not 직장상사리스트[i] in 직속부하딕셔너리:
#         직속부하딕셔너리[직장상사리스트[i]] = [i]
#     else:
#         직속부하딕셔너리[직장상사리스트[i]].append(i)
#
# for i in range(최초칭찬회수):
#     칭찬받은직원, 칭찬받은정도 = map(int, input().split())
#
#     직원큐 = [칭찬받은직원]
#     while 직원큐:
#         칭찬대상직원 = 직원큐.pop(0)
#         칭찬력리스트[칭찬대상직원] += 칭찬받은정도
#         if 칭찬대상직원 in 직속부하딕셔너리:
#             for 칭찬대상직원의부하 in 직속부하딕셔너리[칭찬대상직원]:
#                 직원큐.append(칭찬대상직원의부하)
#
# 칭찬력리스트.pop(0)
# print(칭찬력리스트)


# 2차시도 pypy로 돌려서 비교적 여유롭게 통과
사람수, 최초칭찬회수 = map(int, input().split())
직장상사리스트 = [0] + list(map(int, input().split())) # -1은 상사가 없다는 것을 의미 -> 사장임

칭찬력리스트 = deque([0 for _ in range(사람수+1)])
직속부하딕셔너리 = dict()
for i in range(1, 사람수+1):
    if not 직장상사리스트[i] in 직속부하딕셔너리:
        직속부하딕셔너리[직장상사리스트[i]] = [i]
    else:
        직속부하딕셔너리[직장상사리스트[i]].append(i)

최초칭찬받은직원딕셔너리 = dict()
for i in range(최초칭찬회수):
    칭찬받은직원, 칭찬받은정도 = map(int, input().split())
    if not 칭찬받은직원 in 최초칭찬받은직원딕셔너리:
        최초칭찬받은직원딕셔너리[칭찬받은직원] = 칭찬받은정도
    else:
        최초칭찬받은직원딕셔너리[칭찬받은직원] += 칭찬받은정도

for key, value in 최초칭찬받은직원딕셔너리.items():

    직원큐 = deque()
    직원큐.append(key)
    while 직원큐:
        칭찬대상직원 = 직원큐.popleft()
        if 칭찬대상직원 in 직속부하딕셔너리:
            for 칭찬대상직원의부하 in 직속부하딕셔너리[칭찬대상직원]:
                직원큐.append(칭찬대상직원의부하)

        칭찬력리스트[칭찬대상직원] += value


칭찬력리스트.popleft()
print(*칭찬력리스트)


# n, m = map(int, input().split())
# boss_list = [0] + list(map(int, input().split()))

