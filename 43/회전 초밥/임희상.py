N, d, k, c = map(int, input().split())

sushies = []
for _ in range(N):
    sushies.append(int(input()))

sushies = sushies + sushies[:k]
window = {}
for i in range(k):
    sushi = sushies[i]
    if sushi in window.keys():
        window[sushi] += 1
    else:
        window[sushi] = 1
        
answer = len(window)

for i in range(N):
    
    sushi_out = sushies[i]
    sushi_in = sushies[i+k]

    window[sushi_out] -= 1
    if not window[sushi_out]:
        del window[sushi_out]
    
    if sushi_in in window.keys():
        window[sushi_in] += 1
    else:
        window[sushi_in] = 1
    
    if c in window.keys():
        answer = max(len(window), answer)
    else:
        answer = max(len(window)+1, answer)

print(answer)
