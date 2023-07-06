from bisect import bisect_left

N = int(input())

arr = list(map(int, input().split()))

s = [arr[0]]

for num in arr:
    if num > s[-1]:
        s.append(num)
    else:
        loc = bisect_left(s, num)
        s[loc] = num

print(len(s))

    




