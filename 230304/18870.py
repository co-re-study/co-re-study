import sys
input = lambda : sys.stdin.readline().rstrip('\r\n')
from collections import defaultdict

n = int(input())
points = list(map(int, input().split()))

new_points = sorted(set(points))
points_dict = defaultdict(int)

for i in range(len(new_points)):
    points_dict[new_points[i]] = i

for point in points:
    print(points_dict[point], end=' ')