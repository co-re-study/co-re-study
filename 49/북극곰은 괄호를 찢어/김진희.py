# 북극곰은 괄호를 찢어
n = int(input())
s = input()
answer = 1

if n % 2:  # s가 홀수면 그냥 바로 -1
    answer = -1
else:
    now = 0  # 지금 스택에 들어있는 애가 뭔지 표시
    stack = []
    for i in s:
        if stack:
            # 연속된 괄호는 스택에 추가, 스택의 최대 길이가 곧 날짜
            if i == now:
                stack.append(i)
                answer = max(answer, len(stack))
            else:
                stack.pop()
        else:
            now = i
            stack.append(i)

    # 스택에 짝 없는 애가 남아있다면 실패
    if stack:
        answer = -1

    # 효율성 실패
    # while s:
    #     check = len(s)
    #     s = s.replace('()', '')
    #     s = s.replace(')(', '')
    #     answer += 1
    #     if check == len(s):
    #         answer = -1
    #         break

print(answer)
