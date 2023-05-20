import sys
input = sys.stdin.readline

string = input()
size = len(string)
# 윈도우 크기는 a의 개수
window_size = string.count("a")

start = 0
end = window_size - 1
cnt = string[:window_size].count("a")
answer = window_size - cnt

# 슬라이딩 윈도우
for _ in range(size - 1):
    if string[start] == "a":
        cnt -= 1
    start += 1
    end += 1
    if end == size - 1:
        end = 0
    if string[end] == "a":
        cnt += 1

    # 발견한 a 수가 가장 많은 경우가 정답
    if answer > window_size - cnt:
        answer = window_size - cnt

        
print(answer)
        