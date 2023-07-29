def check(word, left, right, first=1):
    for _ in range((right + 1 - left) // 2):
        if word[left] != word[right]:
            if first and check(word, left, right - 1, 0) and check(word, left + 1, right, 0):
                return 2
            return 1
        left, right = left + 1, right - 1
    return 0

for tc in range(int(input())):
    word = input()
    print(check(word, 0, len(word) - 1))