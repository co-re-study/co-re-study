# 각 검색 키워드를 key로 가진 index를 만들어놓고 찾기 -> 해시테이블?

# def solution(words, queries):
#     answer = []
#     index = dict()

#     for word in words:
#         front_word, back_word = '', ''
#         wild_card = '?' * len(word)
#         if wild_card in index:
#             index[wild_card] += 1
#         else:
#             index[wild_card] = 1
        
#         for word_idx in range(len(word) - 1):
#             wild_card = '?' * (len(word) - word_idx - 1)
            
#             front_word = front_word + word[word_idx]
#             back_word = word[len(word) - word_idx - 1] + back_word
            
#             now_front_word = front_word + wild_card
#             now_back_word = wild_card + back_word
            
#             if now_front_word in index:
#                 index[now_front_word] += 1
#             else:
#                 index[now_front_word] = 1
                
#             if now_back_word in index:
#                 index[now_back_word] += 1
#             else:
#                 index[now_back_word] = 1

#     for query in queries:
#         if query in index:
#             answer.append(index[query])
#         else:
#             answer.append(0)
    
#     return answer

# 효율성 4, 5번 시간초과
# 텍스트 덧셈 하는 과정에서 O(n)을 써서 그런듯. 검색 키워드를 key로 가진 index를 생성하려면 시간초과가 되는 것 같다.

# trie 만들어서 풀기
# 딕셔너리 이용해서 순방향, 역방향 trie 만들고 각 횟수 카운트, 자식 글자 기록

def solution(words, queries):
    answer = []
    trie = dict()
    reverse_trie = dict()
    
    for word in words:
        len_key = str(len(word))
        
        if len_key in trie:
            trie[len_key][""] += 1
        else:
            trie[len_key] = {"": 1}
            
        if len_key in reverse_trie:
            reverse_trie[len_key][""] += 1
        else:
            reverse_trie[len_key] = {"": 1}
            
        target = trie[len_key]
        reverse_target = reverse_trie[len_key]

        for word_idx in range(len(word) - 1):
            if word[word_idx] in target:
                target[word[word_idx]][""] += 1
            else:
                target[word[word_idx]] = {"": 1}
            
            reverse_word_idx = len(word) - word_idx - 1
            if word[reverse_word_idx] in reverse_target:
                reverse_target[word[reverse_word_idx]][""] += 1
            else:
                reverse_target[word[reverse_word_idx]] = {"": 1}
            
            target = target[word[word_idx]]
            reverse_target = reverse_target[word[reverse_word_idx]]
    
    for query in queries:
        if str(len(query)) in trie:
            if len(query) * "?" == query:
                answer.append(trie[str(len(query))][""])
            else:
                if query[0] == "?":
                    target = reverse_trie[str(len(query))]
                    for query_idx in range(len(query) - 1, -1, -1):
                        if query[query_idx] == "?":
                            answer.append(target[""])
                            break
                        elif query[query_idx] in target:
                            target = target[query[query_idx]]
                        else:
                            answer.append(0)
                            break
                else:
                    target = trie[str(len(query))]
                    for query_idx in range(len(query)):
                        if query[query_idx] == "?":
                            answer.append(target[""])
                            break
                        elif query[query_idx] in target:
                            target = target[query[query_idx]]
                        else:
                            answer.append(0)
                            break
        else:
            answer.append(0)
    
    return answer