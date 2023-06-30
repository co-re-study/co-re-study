from itertools import permutations
N = int(input())
target = list(map(int, input().split()))

answer = 0
for permutation in permutations(target):
    # 순열
    current = 0
    nums = set()
    counts = 0
    for num in permutation:
        current += num
        if current < 50:
            nums.add(current)
        elif current == 50:
            counts += 1
        else:
            if current - 50 in nums:
                counts += 1
    answer = max(answer, counts)
print(answer)