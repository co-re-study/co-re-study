# 맨 뒤 인덱스부터 보다가 숫자가 낮아지는 인덱스 구하기
# 해당 인덱스의 숫자를 그 뒤에 있는 숫자 중 다음으로 큰 숫자로 바꾸기
# 그 뒤부터는 오름차순으로 정렬

import sys
input = sys.stdin.readline

testcase = int(input())
for _ in range(testcase):
    num = input().strip()
    # 맨 뒤부터 보다가 숫자 낮아지는 인덱스 구하기
    for idx in range(len(num)-2, -1, -1):
        if num[idx] < num[idx + 1]:
            next_num = 10
            next_idx = idx
            # 숫자가 낮아졌을 때, 그 뒤부터 보면서 그 숫자 다음으로 큰 숫자 구하기
            for j in range(idx, len(num)):
                if int(num[j]) < next_num and int(num[j]) > int(num[idx]):
                    next_num = int(num[j])
                    next_idx = j
            # 위치 변경
            num = num[:idx] + num[next_idx] + num[idx + 1: next_idx] + num[idx] + num[next_idx + 1:]
            # 해당 인덱스 뒤는 정렬해서 출력
            print(num[:idx + 1] + "".join(sorted(list(num[idx+1:]))))
            break
    # 낮아지는 시점이 없으면 가장 큰 숫자임
    else:
        print("BIGGEST")
