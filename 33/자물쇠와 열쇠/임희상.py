def solution(key, lock):
    N = len(lock)
    M = len(key)
    holes = 0
    for i in range(N):
        for j in range(N):
            if not lock[i][j]:
                holes += 1

    for i in range(N):
        lock[i] = [0]*(M-1) + lock[i] + [0]*(M-1)
    lock = [[0]*(N+2*M-2) for _ in range(M-1)] + lock + [[0]*(N+2*M-2) for _ in range(M-1)]
    key_2 = list(map(list, zip(*key[::-1])))
    key_3 = list(map(list, zip(*key_2[::-1])))
    key_4 = list(map(list, zip(*key_3[::-1])))
    def match(r, c, key_type):
        pairs = 0
        for i in range(M):
            for j in range(M):
                if lock[r+i][c+j] and key_type[i][j]:
                    return False
                if M-1 <= r+i <= N+M-2 and M-1 <= c+j <= N+M-2 and not lock[r+i][c+j] and key_type[i][j]:
                    pairs += 1
        if pairs == holes:
            return True
        return False

    for r in range(N+M-1):
        for c in range(N+M-1):
            if match(r, c, key):
                return True
            if match(r, c, key_2):
                return True
            if match(r, c, key_3):
                return True
            if match(r, c, key_4):
                return True
    return False

print(solution([[0, 1, 0], [0, 1, 0], [0, 1, 0]], [[1, 1, 1], [1, 1, 1], [0, 0, 0]]	))
