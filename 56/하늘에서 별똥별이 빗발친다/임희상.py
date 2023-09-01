N, M, L, K = map(int, input().split())

stars = []
for _ in range(K):
    stars.append(list(map(int, input().split())))


stars.sort()
max_counts = 0

for i in range(K):
    start_x, temp1 = stars[i]    
    for j in range(K):
        temp2, start_y = stars[j]
        counts = 0

        for k in range(K):
            current_x, current_y = stars[k]

            if start_x <= current_x <= start_x+L and start_y <= current_y <= start_y+L:
                counts += 1
    
        max_counts = max(max_counts, counts)

print(K - max_counts)
