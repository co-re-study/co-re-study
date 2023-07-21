from itertools import combinations
T = int(input())

for _ in range(T):

    N = int(input())

    targets = list(input().split())
    answer = float('INF')

    for combination in combinations(targets, 3):

        current = 0
        
        for i in range(4):
            if combination[0][i] != combination[1][i]:
                current += 1
            if combination[1][i] != combination[2][i]:
                current += 1
            if combination[2][i] != combination[0][i]:
                current += 1
        
        answer = min(current, answer)
        if not answer:
            break
    
    print(answer)


