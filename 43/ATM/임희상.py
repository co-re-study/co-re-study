N = int(input())

people = sorted(list(map(int, input().split())), reverse = True)

answer = 0
for i in range(N):
    answer += (i + 1) * people[i]

print(answer)
