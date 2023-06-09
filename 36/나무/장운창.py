N, M = map(int,input().split())
line = tuple(map(int,input().split()))
start, end = 0, max(line)
mid = 0
while True:
    mid = (start+end)//2
    rst = sum(x-mid for x in line if x-mid>0)
    if start+1 >= end:
        mid = start
        break
    elif rst > M:
        start = mid+0
    elif rst < M:
        end = mid+0
    else:
        break

print(mid)
