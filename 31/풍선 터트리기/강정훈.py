import heapq
# 1차 시도 결과: 테케 3개 맞고 시간 초과
# 너무 쉽긴 했음 level3 치고
# 정확성 20점
def solution1(a):
    answer = 0
    if len(a) <= 2:
        answer = len(a)
    else:
        answer += 2
        for i in range(1, len(a)-1):
            min_left = min(a[:i])
            min_right = min(a[i+1:])
            if a[i] > min_left and a[i] > min_right:
                continue
            else:
                answer += 1


    return answer

# 이 풀이는 정확성 60점 나옴 테케 9번까지는 맞는데, 그 이후부터 빡셈,
# 말만 안 적어 놨지 효율성 문제라 뒤통수 맞은 기분
def solution2(a):
    answer = 0
    if len(a) <= 2:
        answer = len(a)
    else:
        answer += 2
        min_left = a[0]
        min_right = min(a[2:][:])
        for i in range(1, len(a)-1):
            if a[i] > min_left and a[i] > min_right:
                continue
            else:
                answer += 1

            if min_left > a[i]:
                min_left = a[i]
            if min_right == a[i]:
                min_right = min(a[i+1:])

    return answer

# N차 시도 끝에 성공 (heapq + visited)
# 역시 고수에게 도움을 받는것이 좋다. 이게 팀이지
# heapq라는 것에 대해 제대로 알 수 있는 기회였다.
# a라는 리스트의 길이가 1이나 2일 때는 무조건 모든 풍선이 생존 가능하기 때문에, 그 로직을 써준다.
# visited 개념은 heapq때문에 써줌.
def solution(a):
    answer = 0

    # a의 길이가 1이나 2일 때는 모든 풍선이 다 생존 가능하기 때문에, a의 길이만큼이 정답이다.
    if len(a) <= 2:
        answer = len(a)

    # a의 길이는 3개 이상일 때, 아래의 공식이 유효하다.
    else:
        # answer +=2를 해준 이유는 a의 첫 번째와 마지막 원소는 무조건 생존이 가능하기 때문이다
        # 첫 번째의 원소는 오른쪽 원소들끼리 모두 싸운 이후에 마지막 하나 남은 원소가 무엇이든
        # 하나를 터뜨릴 수 있기 때문에, 무조건 생존 가능하다.
        # 마지막 원소의 원리도 마찬가지다.
        answer += 2

        # right_heap은 초기값이다. 처음에 아래의 for문에서 돌릴 때,
        # a[i]를 기준으로 왼쪽 배열과 오른쪽 배열을 나눠서 비교할 예정이다.
        # 왼쪽 배열에 있는 원소들의 최소값과 오른쪽 배열에 있는 최소값 중
        # 하나보다는 값이 낮아야 풍선이 생존이 가능하다.
        # 따라서 right_heap은 그 배열들의 초기값이라고 볼 수 있다.
        right_heap = a[2:][:]

        # heapq를 이용해 right_heap을 최소값이 가장 앞에 가있는 배열로 바꿔준다.
        heapq.heapify(right_heap)

        min_left = a[0] # 왼쪽 배열의 초기 최소값
        min_right = heapq.heappop(right_heap) # 오른쪽 배열 중 초기 최소값
        visited = set() # for문을 통해 이동할 때마다 visited에 원소를 넣어 줄 예정이다.
        visited.add(min_left) # 초기값으로 a[0]을 넣어줬다.
        for i in range(1, len(a)-1):
            if a[i] > min_left and a[i] > min_right: # 왼쪽 배열의 최소값과 오른쪽 배열의 최소값보다 값이 높기 때문에, 생존 불가능하다.
                pass
            else: # 왼쪽 배열의 최소값 또는 오른쪽 배열의 최소값보다 하나라도 값이 낮다면 그 풍선은 생존할 방법이 존재한다.
                answer += 1

            # 이 문제의 핵심은 왼쪽 배열의 최소값과 오른쪽 배열의 최소값을 갱신시켜주는 로직이다.
            if min_left > a[i]: # for문을 통해 돌면서 min_left를 계속 갱신시켜준다.
                min_left = a[i]

            if min_right == a[i]: # 초기값으로 설정한 최소값에 a[i]가 도달 했을 때, 이제 min_right를 갱신해줘야 된다는 의미다.
                while True:
                    # 이 부분을 놓쳐서, 테스트케이스만 맞고 제출할 때, 계속 틀렸다.
                    # 이런 로직을 짤 때, 예외 케이스다. [-16, 27, 65, -2, 58, -71, -92, -68, -61, -33]
                    # 초기 min_right는 -92이다. 따라서 min_right의 갱신은 -92에 a[i]가 도달했을 때 된다.
                    # 그럴 때 right_heap에서 -92 다음의 최소값을 빼면 -71이 나오는데 -71은 이미 왼쪽 배열에 있다.
                    # 따라서 visited를 찍어주면서, visited에 있으면, 넘기고 오른쪽 배열에 있는 친구들 중 최소값을 꺼내 min_right에 등록시킨다.
                    if right_heap[0] in visited:
                        heapq.heappop(right_heap)
                    else:
                        min_right = heapq.heappop(right_heap)
                        break
            # a[i]에 대한 검증과 왼쪽, 오른쪽 배열 최소값의 갱신이 끝나면, visited에 등록시켜준다.
            visited.add(a[i])

    return answer

a1 = [9,10,-1]
a2 = [-16,27,65,-2,58,-71,-92,-68,-61,-33]
a3 = [1, 3]

