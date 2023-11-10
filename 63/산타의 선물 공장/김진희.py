Q = int(input())
tlst = list(map(int, input().split()))
N, M = tlst[1], tlst[2]

prev = [0]*(N+1)  # 이전 상자 번호
next = [0]*(N+1)  # 다음 상자 번호
w = [0]*(N+1)     # 상자 무게
conv = [0]*(N+1)  # 벨트 번호
head = [0]*(M+1)  # 제일 앞 박스 번호(없으면 0)
tail = [0]*(M+1)  # 제일 끝 박스 번호(없으면 0)
belt_down = [0]*(M+1)  # 벨트 고장
belt_down[0] = 1  # 없는 컨베이어 벨트는 항상 고장!
id_num = {}
num_id = [0]*(N+1)

SIZE = N//M
for i in range(1, N+1):
    if (i - 1) % SIZE != 0:
        prev[i] = i-1
    if i % SIZE != 0:
        next[i] = i+1
    id_num[tlst[2+i]] = i
    num_id[i] = tlst[2+i]
    w[i] = tlst[2+N+i]
    conv[i] = (i-1) // SIZE + 1

for i in range(1, M+1):
    head[i] = (i-1) * SIZE + 1
    tail[i] = i * SIZE


def del_box(idx):
    # 박스 삭제 (위치에 따라 달라짐)
    belt = conv[idx]
    if belt_down[belt] == 1:
        return

    if head[belt] == idx:
        if tail[belt] == idx:   # 1개짜리
            head[belt] = tail[belt] = 0
            belt_down[belt] = 1
        else:                   # head
            head[belt] = next[idx]
            prev[next[idx]] = 0
    elif tail[belt] == idx:     # tail
        tail[belt] = prev[idx]
        next[prev[idx]] = 0
    else:                       # 중간
        prev[next[idx]], next[prev[idx]] = [idx], next[idx]
    num_id[idx] = 0
    next[idx] = prev[idx] = 0
    conv[idx] = 0


def get_idx(id):
    if id in id_num:
        idx = id_num[num]
        if num_id[idx]:
            return idx
    return -1


for q in range(1, Q):

    cmd, num = map(int, input().split())
    if cmd == 200:
        mx = num
        # [1] 각 벨트 제일 앞이 조건 만족하면 꺼내고, 아니면 제일 뒤로
        ans = 0
        for i in range(1, M+1):
            if belt_down[i] == 1:
                continue

            idx = head[i]
            # 빈 벨트
            if idx <= 0:
                continue

            if w[idx] <= mx:
                ans += w[idx]
                del_box(idx)
            else:
                belt = i

                if tail[belt] != idx:
                    head[belt] = next[idx]
                    prev[next[idx]] = 0

                    next[tail[belt]] = idx
                    prev[idx] = tail[belt]
                    next[idx] = 0
                    tail[belt] = idx
        print(ans)

    # 물건 제거
    elif cmd == 300:
        idx = get_idx(num)
        if idx == -1:
            print(-1)
            continue

        belt = conv[idx]
        if belt_down[belt] == 1:
            print(-1)
            continue

        del_box(idx)
        print(num)

    # 물건 확인
    elif cmd == 400:
        idx = get_idx(num)
        if idx == -1:         # 없거나 삭제된 박스면 skip
            print(-1)
            continue

        belt = conv[idx]
        if belt_down[belt] == 1:
            print(-1)
            continue

        h_old, t_old = head[belt], tail[belt]
        if idx == head[belt]:
            pass
        elif idx == tail[belt]:
            next[prev[idx]] = 0
            tail[belt] = prev[idx]
            next[idx], prev[idx] = head[belt], 0
            head[belt], prev[next[idx]] = idx, idx
        else:
            head[belt], tail[belt] = idx, prev[idx]
            prev[idx], next[tail[belt]] = 0, 0
            prev[h_old], next[t_old] = t_old, h_old

        print(belt)

    # 컨베이어 벨트 고장
    elif cmd == 500:
        belt = num
        if belt_down[belt] == 1:   # 이미 고장
            print(-1)
            continue

        idx = head[belt]
        tail_idx = tail[belt]
        belt_down[belt] = 1
        for i in range(belt+1, belt+M+2):
            if belt_down[i % (M+1)] == 0:
                belt = i % (M+1)
                break

        # 제일 뒤에 붙이기
        next[tail[belt]], prev[idx] = idx, tail[belt]
        tail[belt] = tail_idx
        # idx부터 끝까지 컨베이어 벨트 번호 수정
        while idx:
            conv[idx] = belt
            idx = next[idx]
        print(num)
