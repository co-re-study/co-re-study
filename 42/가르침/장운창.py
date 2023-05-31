N, K = map(int,input().split())
if K < 5:
    print(0)
else:
    K -= 5
    study = set(list('aitcn'))
    words = sorted(list(set(input())-study for _ in range(N)), key=lambda x: len(x))
    wordset = set()
    for word in words:
        for w in word:
            wordset.add(w)
    if K >= len(wordset):
        print(N)
    else:
        wordset = list(wordset)
        maxval = 0
        for i in range(1<<len(wordset)):
            if bin(i)[2:].count('1') != K:
                continue
            temp = set()
            for j in range(len(wordset)):
                if i&(1<<j):
                    temp.add(wordset[j])
            val = sum(len(word-temp)==0 for word in words)
            if maxval < val:
                maxval = val
        print(maxval)
