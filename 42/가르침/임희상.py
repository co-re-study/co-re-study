N, K = map(int, input().split())

words = {}
basic = {'a', 'n', 'c', 'i', 't'}
alp = {}
idxs = []
idx = 0

for i in range(N):
    word = input()
    bin_word = 0
    for letter in word:
        if letter in basic:
            continue
        if letter in alp.keys():
            bin_word |= 1 << alp[letter]
            continue
        alp[letter] = idx
        bin_word |= 1 << alp[letter]
        idxs.append(letter)
        idx += 1
    if bin_word in words.keys():
        words[bin_word] += 1
    else:
        words[bin_word] = 1

answer = 0
if K < 5:
    print(0)
else:
    if K-5 >= len(alp):
        print(N)
    else:
        for i in range(1 << len(alp)):
            counts = 0
            for j in range(len(alp)):
                if i & (1 << j):
                    counts += 1
            if counts != K-5:
                continue
            success = 0
            for word in words:
                if i | word == i:
                    success += words[word]
            answer = max(success, answer)

        print(answer)