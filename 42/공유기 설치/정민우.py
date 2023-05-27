import math

def check_house_distance(distance):
    global house_list, C
    acc_dist = 0
    count = 1
    for idx in range(1, len(house_list)):
        acc_dist += house_list[idx] - house_list[idx-1]
        if acc_dist >= distance:
            count += 1
            if count >= C:
                break
            acc_dist = 0
    return True if count >= C else False

N, C = map(int, input().split())

house_list = sorted([int(input()) for _ in range(N)])

l, c, r, min_false = 0, int(house_list[-1] / 2), house_list[-1] + 1, 0

while True:
    if check_house_distance(c):
        if c + 1 == min_false:
            break
        else:
            l, c, r = c + 1, math.ceil((c + r) / 2), r
    else:
        l, c, r, min_false = l, math.ceil(c / 2), c - 1, c

print(c)