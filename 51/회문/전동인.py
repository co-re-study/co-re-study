def is_pseudo(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


n = int(input())
for _ in range(n):
    s = input()
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            if is_pseudo(s, left + 1, right):
                print(1)
                break
            elif is_pseudo(s, left, right - 1):
                print(1)
                break
            else:
                print(2)
                break
        left += 1
        right -= 1
    else:  # 루프가 break 없이 완료된 경우: 회문
        print(0)
