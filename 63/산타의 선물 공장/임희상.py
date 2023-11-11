from bisect import bisect_left
import sys
input = sys.stdin.readline
print = sys.stdout.write
# 이건 안할듯


def find_box(box_id):
    idx = bisect_left(boxes, box_id, key=lambda x: x[0])
    if idx >= len(boxes) or boxes[idx][0] != box_id or not boxes[idx][4]:
        return -1
    return idx


q = int(input())
box_info = list(map(int, input().split()))
n, m = box_info[1], box_info[2]
boxes = []
front_boxes = []
belts = [set() for _ in range(m)]
for i in range(3, 3 + n):
    next_box = box_info[i + 1]
    previous_box = box_info[i - 1]
    if n == m or (i - 2) % (n // m) == 1:
        front_boxes.append(box_info[i])
        previous_box = box_info[i + (n // m) - 1]
    if not (i - 2) % (n // m):
        next_box = front_boxes[-1]
    boxes.append([box_info[i], box_info[i + n], next_box, previous_box, True])
    belts[(i - 3) // (n // m)].add(box_info[i])
boxes.sort()

for _ in range(q - 1):
    command, num = map(int, input().split())
    
    if command == 200:
        acc = 0
        for i in range(m):
            front_box_id = front_boxes[i]
            if front_box_id < 0:
                continue
            box = boxes[find_box(front_box_id)]
            if box[1] <= num:
                acc += box[1]
                box[4] = False
                belts[i].remove(box[0])
                if box[2] == box[0]:
                    front_boxes[i] = -1
                    continue
                next_box = boxes[find_box(box[2])]
                pre_box = boxes[find_box(box[3])]
                pre_box[2], next_box[3] = next_box[0], pre_box[0]
                front_boxes[i] = next_box[0]
            else:
                front_boxes[i] = box[2]
        print(str(acc) + "\n")

    elif command == 300:
        idx = find_box(num)
        if idx == -1:
            print("-1" + "\n")
            continue
        box = boxes[idx]
        print(str(num) + "\n")
        next_box = boxes[find_box(box[2])]
        pre_box = boxes[find_box(box[3])]
        pre_box[2], next_box[3] = next_box[0], pre_box[0]
        box[4] = False
        for i in range(m):
            if box[0] in belts[i]:
                belts[i].remove(box[0])
            if front_boxes[i] == box[0]:
                if box[2] == box[0]:
                    front_boxes[i] = -1
                else:
                    front_boxes[i] = next_box[0]
                break

    elif command == 400:
        idx = find_box(num)
        if idx == -1:
            print("-1" + "\n")
            continue
        box = boxes[idx]
        for i in range(m):
            if box[0] in belts[i]:
                print(str(i + 1) + "\n")
                front_boxes[i] = box[0]
                break

    elif command == 500:
        if front_boxes[num - 1] == -2:
            print("-1" + "\n")
            continue
        print(str(num) + "\n")
        for i in range(1, m):
            i = (num - 1 + i) % m
            if front_boxes[i] == -2:
                continue
            head_box = boxes[find_box(front_boxes[i])]
            tail_box = boxes[find_box(head_box[3])]
            broken_head_box = boxes[find_box(front_boxes[num - 1])]
            broken_tail_box = boxes[find_box(broken_head_box[3])]
            head_box[3], tail_box[2], broken_head_box[3], broken_tail_box[2] = broken_tail_box[0], broken_head_box[0], tail_box[0], head_box[0]
            belts[i] |= belts[num - 1]
            belts[num - 1] = set()
            if front_boxes[num - 1] == -1:
                front_boxes[num - 1] = -2
                break
            front_boxes[num - 1] = -2
            if front_boxes[i] == -1:
                front_boxes[i] = broken_head_box[0]
            break

sys.stdout.flush()
