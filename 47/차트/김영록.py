from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))
if max(arr) > 50:
    print(0)
else:
    ans = 0
    for target in permutations(arr):
        count = 0
        for i in range(N):
            temp = 0
            target *= 2
            for j in range(i, 2*N):
                temp += target[j]
                if temp == 50:
                    count += 1
                    break
                elif temp > 50:
                    break
        ans = max(ans, count)
    print(ans//2)
