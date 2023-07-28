T = int(input())


def check_palindrome(target, left, right):

    while left < right:

        if target[left] != target[right]:
            return(False, (left, right))
        left, right = left+1, right-1
    
    return (True, 0)


for _ in range(T):
    word = input()
    result, idxs = check_palindrome(word, 0, len(word)-1)

    if result:
        print(0)
        continue

    result= check_palindrome(word, idxs[0]+1, idxs[1])[0] or check_palindrome(word, idxs[0], idxs[1]-1)[0]

    if result:
        print(1)
    else:
        print(2)
