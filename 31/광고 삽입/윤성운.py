def solution(play_time, adv_time, logs):
    
    # 실제 시간을 초 단위로 변경
    def make_to_second(time):
        acc = 0
        acc += 3600 * int(time[:2])
        acc += 60 * int(time[3:5])
        acc += int(time[6:])
        return acc
    
    # 초를 실제 시간 단위로 변경
    def make_to_realtime(second):
        hour = str(second // 3600)
        if len(hour) == 1:
            hour = '0' + hour
        second %= 3600
        minute = str(second // 60)
        if len(minute) == 1:
            minute = '0' + minute
        second %= 60
        second = str(second)
        if len(second) == 1:
            second = '0' + second
        return f'{hour}:{minute}:{second}'
        
    # 전체 시간을 초로 변경한 뒤, 초만큼의 길이를 갖는 리스트 생성
    total_time = [0] * (make_to_second(play_time) + 1)
    adv_time = make_to_second(adv_time)
    memo = [[] for _ in range(len(total_time))]
    
    # 만든 리스트에 모든 동영상 시작과 끝 기록
    for log in logs:
        start = make_to_second(log[:8])
        end = make_to_second(log[9:])
        memo[start].append("start")
        memo[end].append("end")
        
    # 현재 시간에 몇 명이 보고 있는지 기록
    viewer = 0
    for time in range(len(total_time)):
        if memo[time]:
            for keyword in memo[time]:
                if keyword == "start":
                    viewer += 1
                elif keyword == "end":
                    viewer -= 1
        total_time[time] = viewer
                    
    # 우선 0초부터 광고 삽입해보기
    answer = "00:00:00"
    acc = 0
    for time in range(adv_time):
        acc += total_time[time]
    max_acc = acc
        
    # 가능한 모든 시간에 광고 삽입해보면서 최대 시청자 수 구하기
    for time in range(len(total_time) - adv_time):
        acc += total_time[time + adv_time] - total_time[time] # 윈도우 슬라이싱
        if acc > max_acc:
            max_acc = acc
            answer = make_to_realtime(time + 1)
    
    return answer