def solution(words, queries):
    
    # 트라이 만들기
    # key: 현재 문자열, value: [다음 문자열 트라이, 각 문자열 수 카운트 딕셔너리]
    # {"f": [{"r": ...}, {5: 4, 6: 1}], "k": ...}
    def make_trie(words):
        trie = dict()
        for word in words:
            target_dict = trie
            for char in word:
                if char not in target_dict:
                    target_dict[char] = [dict(), dict()]
                if len(word) in target_dict[char][1]:
                    target_dict[char][1][len(word)] += 1
                else:
                    target_dict[char][1][len(word)] = 1
                target_dict = target_dict[char][0]
        return trie
    
    
    # 각 검색 키워드 별 답 찾기
    def find_answer(query, trie):
        target_dict = trie
        for idx in range(len(query) - 1):
            if query[idx] not in target_dict or len(query) not in target_dict[query[idx]][1]:
                return 0
            if query[idx + 1] == "?":
                return target_dict[query[idx]][1][len(query)]
            target_dict = target_dict[query[idx]][0]
                
    
    forward_trie = make_trie(words)
    reverse_trie = make_trie(list(map(lambda x: x[::-1], words)))
    
    len_dict = dict()
    for word in words:
        if len(word) in len_dict:
            len_dict[len(word)] += 1
        else:
            len_dict[len(word)] = 1

    answer = []
    for query in queries:
        # 모두 ?인 경우 그 길이를 가진 문자열 수를 append
        if query == "?" * len(query):
            if len(query) in len_dict:
                answer.append(len_dict[len(query)])
            else:
                answer.append(0)
        elif query[-1] == "?":
            answer.append(find_answer(query, forward_trie))
        else:
            answer.append(find_answer(query[::-1], reverse_trie))
            
    return answer