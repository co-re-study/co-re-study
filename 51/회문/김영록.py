def check(l, r):
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return False
    return True


N = int(input())
for _ in range(N):
    s = input()
    left, right = 0, len(s)-1
    if s == s[::-1]:
        print(0)
    else:
        while left < right:
            if s[left] != s[right]:
                cl = check(left+1, right)
                cr = check(left, right-1)
                if cl or cr:
                    print(1)
                    break
                else:
                    print(2)
                    break
            else:
                left += 1
                right -= 1