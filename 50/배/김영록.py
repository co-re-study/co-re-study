N = int(input())
nums = [int(input()) for _ in range(N)]
ap = []
for i in range(1, N):
    target = nums[i] - 1
    for j in ap:
        if not target % j:
            break
    else:
        ap.append(target)
print(len(ap))