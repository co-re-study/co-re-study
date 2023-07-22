
N = int(input())
days = []
candidates = set()
intervals = dict()

for _ in range(N):
    days.append(int(input()))

for day in days[1:]:
    
    if day in candidates:

        for interval in intervals.keys():
            if intervals[interval] == day:
                intervals[interval] = day + interval
                candidates.add(day + interval)

    else:
        intervals[day-1] = day + day-1
        candidates.add(day + day - 1)

print(len(intervals.keys()))
