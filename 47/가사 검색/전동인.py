from collections import defaultdict


def add_word(root, word):
    cur = root
    length = len(word)
    cur[length] += 1
    for ch in word:
        if ch not in cur:
            cur[ch] = defaultdict(int)
        cur = cur[ch]
        cur[length] += 1


def search_word(root, query):
    cur = root
    length = len(query)
    for ch in query:
        if ch == '?':
            return cur[length]
        if ch not in cur:
            return 0
        cur = cur[ch]
    return cur[length]


def solution(words, queries):
    trie = defaultdict(int)
    reversed_trie = defaultdict(int)

    for word in words:
        add_word(trie, word)
        add_word(reversed_trie, word[::-1])

    answer = []
    for query in queries:
        if query[0] == '?':
            answer.append(search_word(reversed_trie, query[::-1]))
        else:
            answer.append(search_word(trie, query))
    return answer
