# 배열의 크기는 2 ** n
# 배열을 절반씩 나누어서 순회
# r, c를 몇 번째로 방문했는지 출력
# 재귀를 사용해서 풀어보자
import sys
input = lambda : sys.stdin.readline().rstrip('\r\n')


def cut(x, y, size):                                      # x, y 좌표와 한변의 길이
    global cnt
    if x > r or x + size <= r or y > c or y + size <= c:  # 해당하는 영역에 원하는 좌표가 없으면
        cnt += size ** 2                                  # 영역의 크기 만큼 카운트에 더함
        return
    if size == 2:                                         # 한변의 길이가 2라면 Z 영역을 구함
        for i in range(2):
            for j in range(2):
                if x + i == r and y + j == c:             # 해당하는 좌표라면
                    print(cnt)                            # cnt 출력 후
                    sys.exit()                            # 프로그램 종료, return을 쓰면 다음 재귀가 돌아가서 안되는 거였음
                else:
                    cnt += 1                              # 아니면 카운트 +1
    else:
        size //= 2                                        # 한변의 길이가 2가 아니면 한변의 길이 반으로 줄이기
        for i in range(2):                                # 4등분한 영역을 순회
            for j in range(2):
                cut(x + size * i, y + size * j, size)     # Z 모양으로 순회 순서 맞추기


n, r, c = map(int, input().split())
cnt = 0
cut(0, 0, 2 ** n)