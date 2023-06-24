W, H, K = map(int, input().split())
N = int(input())
H_cut = [0]+list(map(int, input().split()))+[H]
H_list = [H_cut[i]-H_cut[i-1] for i in range(1, N+2)]
M = int(input())
W_cut = [0]+list(map(int, input().split()))+[W]
W_list = sorted([W_cut[i]-W_cut[i-1] for i in range(1, M+2)])
ans = 0
for i in range(N+1):
    s, e = 0, len(W_list)
    while s < e:
        mid = (s+e)//2
        if H_list[i]*W_list[mid] > K:
            e = mid
        else:
            s = mid+1
    ans += e
print(ans)