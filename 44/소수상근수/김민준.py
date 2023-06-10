import math
N = int(input())




numbers = [False, False] + [True] * (N - 1)

for i0 in range(2 * 2, N + 1, 2):
    numbers[i0] = False
for i1 in range(3,int(math.sqrt(N)),2):
    st = i1
    if numbers[st]==True:
        for i2 in range(st*st, N + 1, st):
            numbers[i2] = False

for i3 in range(7, len(numbers)):
    if numbers[i3]:
        # 상근수 구하기
        visited = dict({})
        stamp = i3
        start = i3
        while 1:
            tmp = 0
            str_num = len(str(start))
            for i4 in range(str_num, 0, -1):
                tmp += (start // (10 ** (i4 - 1))) ** 2
                start = start % (10 ** (i4 - 1))
            if visited.get(tmp,-1) == 1:
                numbers[i3] = False
                break
            elif tmp == 1:
                print(stamp)
                break
            else:
                start = tmp
                visited[tmp] = 1
                continue
