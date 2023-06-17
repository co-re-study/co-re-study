# 키의 개수 n, 퀘스트의 개수 m, 퀘스트 당 사용해야 하는 스킬의 수 k
n, m, k = map(int, input().split())
# 퀘스트 인풋
quests = [list(map(int, input().split())) for _ in range(m)]

subsets = [[]]  # 모든 부분 집합을 다 구하고
max_cnt = 0
for el in quests:
    size = len(subsets)
    for i in range(size):
        temp = subsets[i] + el
        crr_cnt = len(temp) // k  # 현재 부분 집합이 몇 개의 퀘스트 조합인지 카운트
        subsets.append(temp)
        if len(set(temp)) <= n:  # n보다 잡거나 같으면 최대값 비교
            if crr_cnt > max_cnt:
                max_cnt = crr_cnt
print(max_cnt)
