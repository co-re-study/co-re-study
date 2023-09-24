def back_tracking(idx):
    for i in range(1, (idx//2) + 1):
        if s[-i:] == s[-2*i:-i]:
            return -1

    if idx == n:
        for i in s:
            print(i, end="")
        return 0

    for i in range(1, 4):
        s.append(i)
        if back_tracking(idx + 1) == 0:
            return 0
        s.pop()

n = int(input())
s = []
back_tracking(0)