from bisect import bisect_left,bisect_right

def solution(words, queries):
    answer = []
    words_set = [[] for _ in range(10001)]
    rev_words_set = [[] for _ in range(10001)]
    for word in words:
        words_set[len(word)].append(word)
        rev_words_set[len(word)].append(word[::-1])
    for w in words_set:
        w.sort()
    for r in rev_words_set:
        r.sort()
    for query in queries:
        left, right = query.replace('?','a'), query.replace('?','z')
        if query[0] == '?':
            s = bisect_left(rev_words_set[len(query)], left[::-1])
            e = bisect_right(rev_words_set[len(query)], right[::-1])
            answer.append(e-s)
        else:
            s = bisect_left(words_set[len(query)], left)
            e = bisect_right(words_set[len(query)], right)
            answer.append(e-s)
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))


'''
아이디어 생각해보자
중간 없다고 했으니까 3가지 경우
1. 시작
2. 끝
3. 전부

'''