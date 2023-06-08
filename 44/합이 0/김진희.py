import sys
input = sys.stdin.readline

n = int(input())
students = list(map(int, input().split()))
answer = 0
# 일단 정렬
students.sort()
# 첫번째 녀석 뽑기
for i in range(n - 2):
    # 두번째, 세번째 녀석의 합이 첫 녀석을 0으로 만들 수 있는지 확인
    first = students[i]
    left = i + 1
    right = n - 1
    cnt_right = n  # 똑같은 수가 있을 때, 세는 용도
    while left < right:
        if students[left] + students[right] < -first:
            left += 1
        elif students[left] + students[right] > -first:
            right -= 1
        # 세 녀석의 합이 0이 될 때
        else:
            # 두세번째가 같은 수이면 그 사이의 개수만큼 오른쪽 포인터를 옮겨도 가능
            if students[left] == students[right]:
                answer += right - left
            # 두세번째가 다른 수이면 오른쪽 포인터랑 같은 수만큼 가능
            else:
                # 이 때, 왼쪽에서도 계속 똑같은 수가 나올 수 있으니까, 오른쪽 개수를 저장해두고 재사용
                if cnt_right > right:
                    cnt_right = right
                    while cnt_right >= 0 and students[cnt_right - 1] == students[right]:
                        cnt_right -= 1
                # 오른쪽 수의 개수만큼 답에 추가
                answer += right - cnt_right + 1
            # 왼쪽도 한 번 옮겨본다
            left += 1
print(answer)

# from bisect import bisect_left
# # bisect_left(배열, 원소) 첫 번째 해당 원소 인덱스 반환
# # bisect_right(배열, 원소) 해당 원소 다음 인덱스 반환
# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# answer = 0
# for i in range(n-2):
#     left, right = i+1, n-1
#     while left < right:
#         result = arr[i]+arr[left]+arr[right]
#         if result > 0:
#             right -= 1
#         else:
#             if result == 0:
#                 if arr[left] == arr[right]:
#                     answer += right - left
#                 else:
#                     idx = bisect_left(arr, arr[right])
#                     answer += right-idx+1
#             left += 1
# print(answer)