import sys
input = sys.stdin.readline

n, s = map(int, input().split())
m = int(input())
eating_rate = [0] * m # 각 사람별 먹는 시간
time_to_eat = [0] * m # 각 사람별 다음으로 소보루를 집을 시간
candidates = {0} # 소보루 없앨 수 있는 시간들

# 각 사람별로 먹는 시간 저장
for i in range(m):
    eating_rate[i] = int(input())
    
bread = 0
time = 0
last_person = 0
flag = True


while flag:
    for person in range(m):
        if time_to_eat[person] == time:
            bread += 1
            # 목표치만큼 빵을 다 먹었다면 break
            if bread == n - s:
                last_person = person + 1
                flag = False
                break
            time_to_eat[person] = time + eating_rate[person]
            candidates.add(time + eating_rate[person]) # 다음 시간 저장
            candidates.discard(time) # 현재 시간 삭제

    # 소보루 없앨 수 있는 시간에서만 for문 돌기
    while time not in candidates:
        time += 1

print(last_person)

