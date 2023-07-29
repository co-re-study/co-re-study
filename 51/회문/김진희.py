# 회문
def pseudo_palindrome(w):
    for k in range(len(w)//2):
        if w[k] != w[-k-1]:
            return 2
    else:
        return 1


for tc in range(1, int(input()) + 1):
    word = input()
    answer = 2
    for i in range(len(word) // 2):
        if word[i] != word[len(word)-1-i]:
            # 회문아님
            answer = min(pseudo_palindrome(word[i + 1:len(word)-i]), pseudo_palindrome(word[i:len(word)-i-1]))
            break
    # for문이 break없이 무사히 끝났다면 그냥 회문
    else:
        answer = 0

    print(answer)