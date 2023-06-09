import sys
input = sys.stdin.readline

# 1차시도 시간초과

N = int(input())

sosu_list = []
sosu_set = set()
for i in range(7, N+1):
    flag = False
    for j in range(2, i):
        if i % j == 0:
            flag = True
            break
    if not flag:
        sosu_list.append(i)
        sosu_set.add(i)

for i in sosu_list:
    default_set = set()
    default_set.add(i)
    candi = str(i)
    is_sangguen = False
    while True:
        answer = 0
        for j in range(len(candi)):
            answer += int(candi[j])**2
        if answer == 1:
            is_sangguen = True
            break
        elif answer in default_set:
            break
        default_set.add(answer)
        candi = str(answer)
    if is_sangguen == True and i in sosu_set:
        print(i)

# 2차시도 N의 범위가 100만이기떄문에 첫번째 소수 찾는 for문에서 i가 1000이 넘어가는 경우에 1000까지만 돌도록 제한을 둠
# 왜냐하면 100만의 제곱근이 1000이기 떄문임.
# 그렇게 범위를 줄이니 통과하긴 함

N = int(input())

sosu_list = []
sosu_set = set()
for i in range(7, N+1):
    flag = False
    if i > 1001:
        for j in range(2, 1001):
            if i % j == 0:
                flag = True
                break
    else:
        for j in range(2, i):
            if i % j == 0:
                flag = True
                break
    if not flag:
        sosu_list.append(i)
        sosu_set.add(i)

for i in sosu_list:
    default_set = set()
    default_set.add(i)
    candi = str(i)
    is_sangguen = False
    while True:
        answer = 0
        for j in range(len(candi)):
            answer += int(candi[j])**2
        if answer == 1:
            is_sangguen = True
            break
        elif answer in default_set:
            break
        default_set.add(answer)
        candi = str(answer)
    if is_sangguen == True and i in sosu_set:
        print(i)

