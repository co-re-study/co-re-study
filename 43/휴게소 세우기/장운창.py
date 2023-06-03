N, M, L = map(int,input().split())
if N:
    line = sorted(list(map(int,input().split()))) + [L]
else:
    line = [L]
start = 0
end = L
val = 0
while end-start>1:
    mid = (start+end)//2
    prev = 0
    cnt = M
    for i in line:
        target = i-prev
        if target > mid:
            dival = 2
            worked = False
            while cnt >= dival-1:
                if target%dival:
                    if target//dival+1 <= mid:
                        worked = True
                        cnt -= dival-1
                        break
                else:
                    if target//dival <= mid:
                        worked = True
                        cnt -= dival-1
                        break
                dival += 1
            if not worked:
                break
        prev = i
    else:
        # 통과
        end = mid
        val = end
        continue
    # 안통과
    start = mid
print(val)
