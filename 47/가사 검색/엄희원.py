def solution(words, queries):
    answer = []
    trie = dict()
    retrie = dict()
    for word in words:
        if len(word) not in trie:
            trie[len(word)] = {}
        curr = trie[len(word)]

        for w in word:
            if w not in curr:
                curr[w] = [1, {}]
            elif w in curr:
                curr[w][0] += 1

            curr = curr[w][1]

    for word in words:
        word = word[::-1]
        if len(word) not in retrie:
            retrie[len(word)] = {}
        curr = retrie[len(word)]

        for w in word:
            if w not in curr:
                curr[w] = [1, {}]
            elif w in curr:
                curr[w][0] += 1

            curr = curr[w][1]

    for query in queries:
        answer.append(0)
        if query[-1] == '?' and query[0] == '?':
            if len(query) in trie:
                cnt = 0
                for key in trie[len(query)]:
                    cnt += trie[len(query)][key][0]
                answer[-1] = cnt

        elif query[-1] == '?':
            if len(query) in trie:
                cur = trie[len(query)]
                for q in range(len(query)):

                    if query[q] == '?':
                        answer[-1] = cur[0]
                        break
                    elif q == 0 and query[q] in cur:
                        cur = cur[query[q]]
                    elif query[q] in cur[1]:
                        cur = cur[1][query[q]]
                    else:
                        break

        elif query[0] == '?':
            query = query[::-1]
            if len(query) in retrie:
                cur = retrie[len(query)]
                for q in range(len(query)):
                    if query[q] == '?':
                        answer[-1] = cur[0]
                        break
                    elif q == 0 and query[q] in cur:
                        cur = cur[query[q]]
                    elif query[q] in cur[1]:
                        cur = cur[1][query[q]]
                    else:
                        break
    return answer