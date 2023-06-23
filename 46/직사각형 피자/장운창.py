W, H, K = map(int,input().split())
N = int(input())
hline = (0, *(map(int,input().split())), H)
hline = sorted(list(hline[x+1]-hline[x] for x in range(len(hline)-1)))
M = int(input())
vline = (0, *(map(int,input().split())), W)
vline = sorted(list(vline[x+1]-vline[x] for x in range(len(vline)-1)))
answer = 0
for i in hline:
    S, E = 0, len(vline)
    target = K//i
    mid = 0
    flag = False
    while S+1 != E:
        mid = (S+E)//2
        if vline[mid] <= target:
            S = mid
            flag = False
        else:
            E = mid
            flag = True
    if flag:
        mid -= 1
    if vline[mid] <= target:
        answer += mid+1
print(answer)
