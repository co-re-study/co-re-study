# import sys
# input = sys.stdin.readline
n, s = map(int, input().split())
m = int(input())
a = [int(input()) for _ in range(m)]
b, t = 0, 0
while True:
    for i in range(m):
        if not t % a[i]:
            b += 1
            if b >= n-s:
                print(i+1)
                exit()
    t += 1