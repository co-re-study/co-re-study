originword = input()
bcnt = originword.count('b')
if 'b' not in originword or 'a' not in originword:
    print(0)
else:
    mincnt = 1001
    word = originword[:]
    wordset = set()
    for _ in range(len(originword)):
        if word[0] == 'b':
            wordset.add(word)
        word = word[-1] + word[:-1]

    for word in wordset:
        word = list(word)
        idx = word.index('b')
        bidx = word[::-1].index('b')
        bidx = len(word)-bidx-1
        cnt = 0
        while True:
            while word[bidx] == 'b':
                bidx -= 1
            if idx+1 > bidx:
                break
            word[idx], word[bidx] = word[bidx], word[idx]
            cnt += 1
            idx = word.index('b')
        if mincnt > cnt:
            mincnt = cnt
        word = word[::-1]
    print(mincnt)