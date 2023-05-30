# 정렬 후 누적합

N, P = int(input()), sorted(map(int, input().split()))
print(sum(list(map(lambda x: sum(x), list(map(lambda x: P[:x], range(N, -1, -1)))))))