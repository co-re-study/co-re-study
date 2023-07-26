# abbbac
# 0, 5번째에서 다름
# 1. 1~5로 잘라서 회문인지 확인
# 2. 0~4로 잘라서 회문인지 확인
# 1, 2번 중 하나라도 True라면 유사회문
# 둘 다 False라면 일반 문자열

import sys
input = sys.stdin.readline

def check_palindrome(start, end):
    while start < end:
        # 회문이 아니면 False 출력하고 달랐던 지점 반환
        if string[start] != string[end]:
            return False, start, end
        start += 1
        end -= 1
    # 회문이면 True 출력하고 False일 때와 형식 맞춰서 반환
    return True, 0, 0

T = int(input())
for _ in range(T):
    string = input().strip()
    is_palindrome, start, end = check_palindrome(0, len(string) - 1)
    # 회문이면 0 출력
    if is_palindrome:
        print(0)
        continue
    # 유사회문이면 1 출력
    if check_palindrome(start + 1, end)[0] or check_palindrome(start, end - 1)[0]:
        print(1)
        continue
    # 아니면 2 출력
    print(2)
