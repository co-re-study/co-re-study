'''
union-find 문제
해당하는 두 원소의 각각의 root를 찾고 그게 같다면 로직을 끝낸다.
'''
import sys
input = sys.stdin.readline


def find_root(x):
    if x != nums[x]:  # 루트 찾아야 하는 경우 (그냥 자기가 루트면 찾을 필요x)
        nums[x] = find_root(nums[x])  # 계속 들어가자
    return nums[x]


n, m = map(int, input().split())
nums = [i for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    if find_root(a) == find_root(b):
        print(i+1)
        break
    s, e = min(find_root(a), find_root(b)), max(find_root(a), find_root(b))
    nums[e] = s
else:
    print(0)