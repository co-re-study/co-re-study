# 가장 가까운 세 사람의 심리적 거리
for tc in range(int(input())):
    char_set = {'ISTJ': 0, 'ISFJ': 0, 'INFJ': 0, 'INTJ': 0, 'ISTP': 0, 'ISFP': 0, 'INFP': 0, 'INTP': 0, 'ESTP': 0, 'ESFP': 0, 'ENFP': 0, 'ENTP': 0, 'ESTJ': 0, 'ESFJ': 0, 'ENFJ': 0, 'ENTJ': 0}
    students = int(input())  # 학생 수
    mbtis = input().split()
    answer = 98765432123456789

    # 똑같은 게 3개면 거리가 0
    for mbti in mbtis:          # 입력 받은 mbti 수만큼 연산 최대 십만
        char_set[mbti] += 1
    for check in char_set:      # 16번 연산
        if char_set[check] >= 3:
            print(0)
            break

    # 무조건 세 사람을 봐야할 때
    else:
        for i in range(students):
            for j in range(i + 1, students):
                for z in range(j + 1, students):
                    ans = 0
                    for c in range(4):
                        if mbtis[i][c] == mbtis[j][c] == mbtis[z][c]:
                            continue
                        else:
                            ans += 2
                            if ans >= answer:
                                break
                    else:
                        if ans < answer:
                            answer = ans
        print(answer)

