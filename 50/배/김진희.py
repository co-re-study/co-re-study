# 배
days = int(input())
first = int(input())
happy = []                          # 딕셔너리로 값까지 확인했는데, 그냥 리스트로 % 나머지만 확인해도 된다.
answer = 0
for _ in range(days - 1):
    today = int(input())
    for i in happy:
        if not (today - 1) % i:
            break                   # break를 까먹으면 말도 안 돼
    else:                           # 뎁스를 더 넣어서 틀렸
        happy.append(today - 1)
        answer += 1

print(len(happy))