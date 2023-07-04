import sys
input = sys.stdin.readline

# 현재 숫자 자리의 오른쪽 숫자와 교체
def binary_search(num):
    left = 0
    right = len(lis)
    while left < right:
        middle = (left + right) // 2
        if lis[middle] < num:
            left = middle + 1
        else:
            right = middle
    return right

N = int(input())
nums = list(map(int, input().split()))

lis = [nums[0]]
for num in nums[1:]:
    
    # 제일 큰 숫자면 lis에 추가
    if num > lis[-1]:
        lis.append(num)

    # 가장 작은 숫자면 0번째 인덱스 교체
    elif num <= lis[0]:
        lis[0] = num

    # 나머지는 이진 탐색으로 자리 찾아 교체
    else:
        lis[binary_search(num)] = num

print(len(lis))