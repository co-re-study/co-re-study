def find_langford(arr, idx, cnt, memo):
    global answer

    # arr 다 채운 경우
    if cnt == n:
        if len(memo) == n:
            answer += 1
        return
    
    # arr 다 채우기 전에 인덱스가 끝에 도달한 경우
    if idx == n * 2:
        return
    
    # 해당 인덱스에 값이 이미 있으면 다음 인덱스로
    if arr[idx]:
        find_langford(arr, idx + 1, cnt, memo)
        return
    
    # x - 1, y - 1번째 자리에 y - x - 1로 채우기
    if idx == x - 1:
        arr = arr[:]
        arr[idx] = y - x - 1
        arr[idx + y - x] = y - x - 1
        memo = set(memo)
        memo.add(y - x - 1)
        find_langford(arr, idx + 1, cnt + 1, memo)
        return
    
    # 모든 숫자 보면서 현재 인덱스와 숫자만큼 건너뛴 인덱스 채우기
    for num in num_list:
        if num == y - x - 1 or num in memo:
            continue
        if idx + num + 1 < n * 2:
            if arr[idx + num + 1] or idx + num + 1 == x - 1 or idx + num + 1 == y - 1:
                continue
            tmp_arr = arr[:]
            tmp_arr[idx] = num
            tmp_arr[idx + num + 1] = num
            tmp_memo = set(memo)
            tmp_memo.add(num)
            find_langford(tmp_arr, idx + 1, cnt + 1, tmp_memo)


n, x, y = map(int, input().split())
num_list = list(range(1, n + 1))
arr = [0] * (n * 2)
answer = 0
find_langford(arr, 0, 0, {})

print(answer)