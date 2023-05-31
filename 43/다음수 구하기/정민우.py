for tc in range(int(input())):
    A = input()
    next_idx = (len(A) - 1, 0)
    for idx in range(len(A)):
        from_idx = len(A) - idx - 1
        if from_idx <= next_idx[1]:
            break
        for to_idx in range(len(A) - idx - 2, -1, -1):
            if to_idx == next_idx[1]:
                break
            if to_idx > next_idx[1] and int(A[from_idx]) > int(A[to_idx]):
                next_idx = (from_idx, to_idx)
                break

    if next_idx == (len(A) - 1, 0):
        print("BIGGEST")
    else:
        print(A[:next_idx[1]] + A[next_idx[0]] + ''.join(sorted(list(A[next_idx[1]:next_idx[0]] + A[next_idx[0] + 1:]))))