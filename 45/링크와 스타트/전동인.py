n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
allsets = [i for i in range(n)]

min_diff = 100*n*n
subsets = [[]]
for i in range(n):
    size = len(subsets)
    for j in range(size):

        tmp = subsets[j][:] + [i]
        subsets.append(tmp)

        sub = [i for i in allsets if i not in tmp]  # 반대되는 부분 집합 구하기

        tmp_score = 0
        tmp_len = len(tmp)
        for x in range(tmp_len-1):
            for y in range(x+1, tmp_len):
                tmp_score += matrix[tmp[x]][tmp[y]] + matrix[tmp[y]][tmp[x]]

        sub_score = 0
        sub_len = len(sub)
        for x in range(sub_len-1):
            for y in range(x+1, sub_len):
                sub_score += matrix[sub[x]][sub[y]] + matrix[sub[y]][sub[x]]

        diff = abs(tmp_score-sub_score)
        if diff < min_diff:
            min_diff = diff

print(min_diff)
