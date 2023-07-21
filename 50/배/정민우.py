N, _ = int(input()), input()
boats = set()
for _ in range(N - 1):
    day = int(input()) - 1
    flag = True
    for boat in boats:
        if not day % boat:
            flag = False
            break
    if flag:
        boats.add(day)
print(len(boats))
