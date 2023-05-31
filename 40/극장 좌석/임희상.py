N = int(input())
M = int(input())

seats = [0] * (N+1)
for _ in range(M):
    seat_num = int(input())
    seats[seat_num] = seat_num

counts = [0, 1, 2, 3]
streak = 0
streaks = []
for i in range(1, N+1):
    
    if seats[i]:
        streaks.append(streak)
        streak = 0
    else:
        streak += 1
        if len(counts) > streak:
            counts.append(counts[-1]+counts[-2])
if not seats[N]:
    streaks.append(streak)
answer = 1
for streak in streaks:
    if streak:
        answer *= counts[streak]
print(answer)