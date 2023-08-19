def sum_seq(n):
    return n * (n + 1) // 2


N, arr = int(input()), list(map(int, input().split()))
seq, overlap, ans = [], 0, 0

for i in range(N):
    if arr[i] not in seq:
        seq.append(arr[i])
    else:
        count = len(seq)
        while True:
            seq.pop(0)
            if arr[i] not in seq:
                ans += sum_seq(count) - sum_seq(overlap)
                overlap = len(seq)
                seq.append(arr[i])
                break
ans += sum_seq(len(seq)) - sum_seq(overlap)

print(ans)
