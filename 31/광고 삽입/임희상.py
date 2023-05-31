def solution(play_time, adv_time, logs):
    # 문제에서 준 시간을 모두 초단위로 통일
    # 전체 playtime의 매 초마다 몇 명이 시청중인지 계산
    # 1초부터 가능한 모든 광고시간동안 시청시간 합계를 계산(슬라이딩 윈도우)
    # 가장 높은 시작시간이 정답
    answer = ''
    times = []
    starts = {}
    ends = {}
    adv_time = list(map(int, adv_time.split(':')))
    adv_time = adv_time[0] * 3600 + adv_time[1] * 60 + adv_time[2]
    play_time = list(map(int, play_time.split(':')))
    play_time = play_time[0] * 3600 + play_time[1] * 60 + play_time[2]
    total_time = [0] * play_time

    for log in logs:
        start, end = log.split('-')
        start = list(map(int, start.split(':')))
        start = start[0] * 3600 + start[1] * 60 + start[2]
        end = list(map(int, end.split(':')))
        end = end[0] * 3600 + end[1] * 60 + end[2]
        if start in starts.keys():
            starts[start].append(end)
        else:
            starts[start] = [end]
            times.append(start)
        if end in ends.keys():
            ends[end].append(start)
        else:
            ends[end] = [start]
            times.append(end)
    times.sort()
    viewers = 0
    for i in range(play_time):
        if i in starts.keys():
            viewers += len(starts[i])
        if i in ends.keys():
            viewers -= len(ends[i])
        total_time[i] += viewers

    window = sum(total_time[:adv_time])
    max_sum = window
    target = 0
    for i in range(play_time-adv_time):
        window += - total_time[i] + total_time[i+adv_time]
        if window > max_sum:
            max_sum = window
            target = i+1
    h = str(target // 3600)
    if len(h) == 1:
        h = '0' + h
    target %= 3600
    m = str(target // 60)
    if len(m) == 1:
        m = '0' + m
    target %= 60
    s = str(target)
    if len(s) == 1:
        s = '0' + s
    answer = f'{h}:{m}:{s}'
    return answer

solution("02:03:55", "00:14:15",
         ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
