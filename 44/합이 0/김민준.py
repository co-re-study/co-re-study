import sys
input = sys.stdin.readline
N = int(input())

coding_level = list(map(int,input().split()))

coding_level.sort()

ans = 0
for i0 in range(N-2):
    first = -coding_level[i0]
    left = i0+1
    right = N-1
    mx_idx = N
    while left<right:
        tmp = coding_level[left] + coding_level[right]
        if first == tmp:
            #두 수가 같다
            if coding_level[left] == coding_level[right]:
                ans += right - left
            #두 수가 다르다
            else:
                if mx_idx > right:
                    mx_idx = right
                    while mx_idx>=0 and coding_level[mx_idx-1]==coding_level[right]:
                        mx_idx -= 1
                ans += right - mx_idx + 1
            left += 1
        elif first < tmp:
            right -= 1
        else:
            left += 1
print(ans)







