def solution(words, queries):
    answer = []
    trie = {}
    reverse_trie = {}
    for word in words:
        length = len(word)
        idx = 0
        current = trie
        current_reverse = reverse_trie
        
        while length > idx:
            if length-idx in current:
                current[length-idx] += 1
            else:
                current[length-idx] = 1
            if length-idx in current_reverse:
                current_reverse[length-idx] += 1
            else:
                current_reverse[length-idx] = 1
            
            if word[idx] in current:
                current = current[word[idx]]
            else:
                current[word[idx]] = {}
                current = current[word[idx]]
            if word[-1-idx] in current_reverse:
                current_reverse = current_reverse[word[-1-idx]]
            else:
                current_reverse[word[-1-idx]] = {}
                current_reverse = current_reverse[word[-1-idx]]
            idx += 1
    
    for query in queries:
        if query[0] == '?':
            target = query[::-1]
            current = reverse_trie
        else:
            target = query
            current = trie
        idx = 0
        flag = False
        while target[idx] != '?':
            if target[idx] not in current.keys():
                answer.append(0)
                flag = True
                break
            current = current[target[idx]]
            idx += 1
        if flag:
            continue
        if len(query)-idx in current.keys():
            answer.append(current[len(query)-idx])
        else:
            answer.append(0)
            
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["?????", "????","fro??", "????o", "fr???", "fro???", "pro?"]))