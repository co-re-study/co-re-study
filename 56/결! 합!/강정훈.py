from itertools import combinations


def is_gyul(shapes):
    if shapes[0] == shapes[1] == shapes[2]:
        return True
    elif shapes[0] != shapes[1] and shapes[1] != shapes[2] and shapes[0] != shapes[2]:
        return True
    else:
        return False


hap_set = set()
figure_list = [["0", "0", "0"]]+[input().split() for _ in range(9)]
for candidate in combinations(range(1, 10), 3):
    shapes = figure_list[candidate[0]][0], figure_list[candidate[1]][0], figure_list[candidate[2]][0]
    inner_colors = figure_list[candidate[0]][1], figure_list[candidate[1]][1], figure_list[candidate[2]][1]
    outter_colors = figure_list[candidate[0]][2], figure_list[candidate[1]][2], figure_list[candidate[2]][2]
    if is_gyul(shapes) and is_gyul(inner_colors) and is_gyul(outter_colors):
        hap_set.add(candidate)

N = int(input())
already_hap = set()
gyul = False
answer = 0
for i in range(N):
    router = input().split()
    if router[0] == 'H':
        candidate = tuple(sorted([int(router[1]), int(router[2]), int(router[3])]))
        if candidate in hap_set and candidate not in already_hap:
            answer += 1
            already_hap.add(candidate)
        else:
            answer -= 1
    else:
        if hap_set == already_hap and not gyul:
            answer += 3
            gyul = True
        else:
            answer -= 1

print(answer)


