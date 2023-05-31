# 효율성 통과 안될 줄 알고 일단 풀어봄.
# 당연히 1차에서는 실패 뜸 NlogN으로 가야할듯

def solution1(stones, k):
    answer = 0
    jump = 0
    while True:
        for i in range(len(stones)):
            if stones[i] > 0:
                jump = 0
                stones[i] = stones[i] - 1
            else:
                jump += 1
            if jump == k:
                break
        if jump == k:
            break
        else:
            answer += 1

    return answer


# 2차 시도 효율성 테스트 실패 발생 2중 for문이긴하지만,
# 2번째 for문의 길이가 stones와 공유를 하고 있기 때문에, 몇개는 통과할 수 있을 줄 알았는데, 안됨
# NlogN방식을 결국에는 고려해 봐야 할 것 같다.

def solution2(stones, k):
    answer = 0
    chance = 9999999999999999999
    for i in range(len(stones)-k + 1):
        stones[i]
        answer_candidate = 0
        for j in range(k):
            if stones[i+j] > answer_candidate:
                answer_candidate = stones[i+j]
        if answer_candidate <= chance:
            chance = answer_candidate
    answer = chance
    return answer

# 3차 시도 성공 (이진 탐색)
# 2차 시도 때의 개념을 NlogN으로 시간을 줄이는 방식으로 적용시키면 된다.
# 이럴 때의 가장 흔하게 사용할 수 있는 방법이 이진탐색이다.
# left를 돌에서 나올 수 있는 가장 작은 수를 설정한다.
# right를 돌에서 나올 수 있는 가장 큰 수를 설정한다.
# k는 점프를 하여 이미 가라앉은 디딤돌을 무시하고 넘을 수 있는 거리이다.

def solution(stones, k):
    answer = 0
    left = 1 # stones의 배열에서 가장 작은 수
    right = 200000000 # stones의 배열에서 가장 큰 수
    while left <= right: # 이진탐색의 기본인 left가 right보다 커지면 그 지점이 우리가 찾던 값이다.
        mid = (left + right) // 2 # 이진 탐색의 mid를 정해줌
        cnt = 0
        # cnt는 mid보다 작은 돌이 얼마나 연속적으로 있는지 세는 의미이다.
        # 예를 들어, 예제에 나온 stones에서 k는 3이고, 처음 탐색하는 곳의 돌들은 우선 2,4,5를 탐색하게 된다.
        # 따라서 mid가 5와 가까운 값을 가질 때 까지 계속 right의 값은 1/2이 되고, 그에 맞춰 mid의 값도 줄어든다.
        for stone in stones:
            # 돌에 적힌 숫자가 mid보다 크면 cnt를 0으로 초기화 한다.
            if stone > mid:
                cnt = 0
            # 돌에 적힌 숫자가 mid보다 작거나 같으면 cnt를 지속적으로 늘려준다.
            else:
                cnt += 1

            # cnt와 k가 같아졌다는 말은 mid의 값이 크다는 의미와 같아서, right를 줄여준다.
            if cnt == k:
                right = mid - 1
                break
        # stones 배열을 다 돌았는데, cnt가 결국 k보다 크다면 left를 늘려준다.
        if cnt < k:
            left = mid + 1
    answer = left
    return answer
    # 이해가 안되면 파이참 디버깅모드로 예제에 나와있는 값들을 넣고 와일문을 돌려보면 이해가 잘 됨.

stones = [2, 4, 5, 3, 2, 1, 3, 2, 5, 1]
k = 3
print(solution(stones, k))