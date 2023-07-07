# C부터 거리
# 0 = A, 1 = B...
A = ["A", "B", "C", "D", "E", "F", "G"]
R = [2, 1, 2, 2, 1, 2, 2]
L = [2, 2, 1, 2, 2, 1, 2]

n = int(input())
lst = [int(input()) for _ in range(n)]


def isTrue(crr, v):  # 검증
    next = crr
    tmp = v

    if tmp == 0:
        return next
    elif tmp > 0:
        while tmp > 0:
            tmp -= R[next]
            next = index(next + 1)

        if tmp == 0:
            return next
        else:
            return -1

    elif tmp < 0:
        while tmp < 0:
            tmp += L[next]
            next = index(next - 1)

        if tmp == 0:
            return next
        else:
            return -1


def index(tmp):  # 인덱스 순환
    if tmp >= 7:
        return tmp - 7
    elif tmp < 0:
        return tmp + 7
    else:
        return tmp


# c부터 시작
for s in range(7):
    crr = s
    for el in lst:
        next = isTrue(crr, el)
        if next == -1:
            break
        crr = next
    else:
        print(A[s], A[crr])
