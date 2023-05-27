# 각 자리에서 네 방향으로 이동하는 함수 생성

def move(i, j, n, num):
    # 여섯 자리 찾았으면 함수 종료
    if n == 6:
        # 숫자 조합 처음 찾았다면 리스트에 추가
        if num not in num_list:
            num_list.append(num)
        return

    # 각 네 방향으로 들어가기
    if 0 <= i < 5 and 0 <= j < 5:
        move(i + 1, j, n + 1, num + arr[i][j])
        move(i - 1, j, n + 1, num + arr[i][j])
        move(i, j + 1, n + 1, num + arr[i][j])
        move(i, j - 1, n + 1, num + arr[i][j])

arr = [input().split() for _ in range(5)]
num_list = []

# 각 자리에 대해 모두 함수 실행
for p in range(5):
    for q in range(5):
        move(p, q, 0, '')

# 찾은 조합 개수 출력
print(len(num_list))