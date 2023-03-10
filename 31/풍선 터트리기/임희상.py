def solution(a):
    # 배열 내의 어떤 인덱스를 기준으로
    # [왼 쪽] 그녀석 [오른 쪽]이라 할 수 있다.
    # 지정한 값이 [왼 쪽]의 최솟값, [오른 쪽]의 최솟값보다 모두 크면 
    # 양측의 풍선을 모두 터뜨릴 수 없게 되니 살아남을 수 없다.
    # 인덱스를 앞에서 한 번, 뒤에서 한 번 돌면서 현재까지의 최솟값이 나보다 작은지 확인
    answer = min(len(a), 2)
    possibles = [False] * len(a)
    left_min = a[0]
    for i in range(1, len(a)-1):
        number = a[i]
        if number < left_min:
            possibles[i] = True
            left_min = number
    right_min = a[-1]
    for i in range(len(a)-2, 0, -1):
        number = a[i]
        if number > right_min:
            if possibles[i]:
                answer += 1
        else:
            answer += 1
            right_min = number
                
    return answer