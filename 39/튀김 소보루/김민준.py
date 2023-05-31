import sys

input = sys.stdin.readline

n, s = map(int,input().split())
ans_num = n - s
m = int(input())
cost_time = list()
#걸리는 시간
for _ in range(m):
    cost_time.append(int(input()))
soboroo = m
time = 0
#소보로가 구하려는 num보다 클 경우
if soboroo >= ans_num:
    print(ans_num)
else:
#소보로가 구하려는 num보다 작은 경우
    temp = list()
    while True:
        time += 1
        for i1 in range(m):
            if time % cost_time[i1] == 0:
                temp.append(i1+1)
        soboroo += len(temp)
        if ans_num <= soboroo:
            ans_idx = ans_num - soboroo - 1
            print(temp[ans_idx])
            break
        else:
            temp = []
