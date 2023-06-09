def solution(n):
    maxval = n*(n+1)//2
    answer = [0 for x in range(maxval)]
    idx = 0
    initamp = 0
    amp = 1
    flag = True
    straight = False
    for num in range(1, maxval+1):
        answer[idx] = num
        if idx+amp >= maxval or (flag and idx+amp < maxval and answer[idx+amp]):
            straight = True
        elif not flag and answer[idx-amp]:
            initamp += 2
            amp = initamp
            flag = True
        if straight:
            if idx+1 >= maxval or (idx+1 < maxval and answer[idx+1]):
                straight = False
                flag = False
                idx -= amp
                amp -= 1
            else:
                idx += 1
        else:
            if flag:
                idx += amp
            else:
                idx -= amp
            if flag:
                amp += 1
            else:
                amp -= 1
    return answer
