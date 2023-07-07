from collections import defaultdict


def solution(words, queries):
    answer = []
    wordDict = defaultdict(int)  # 물음표가 뒤에 있을 때 사용
    dictWord = defaultdict(int)  # 물음표가 앞에 있을 때 사용

    # [1] 단어 사전에 추가하기
    for word in words:
        add_word(word, wordDict)
        add_word(word[::-1], dictWord)

    # [2] 검색 키워드 찾기
    for query in queries:
        if query[0] == "?":  # '?'로 시작하면 뒤에서부터 검색
            answer.append(find_word(query[::-1], dictWord))
        else:                # 앞에서부터 검색
            answer.append(find_word(query, wordDict))

    return answer


# 두 함수 재귀로 하니까 효율성 두 문제 통과 못함 ㅜㅜ 모두 for문으로 바꾸고 통과
def add_word(x, d):
    d = d
    for char in range(len(x)):
        d[len(x) - char] += 1
        # 알파벳이 없으면 생성
        if not d[x[char]]:
            d[x[char]] = defaultdict(int)
        d = d[x[char]]


def find_word(x, d):
    d = d
    for char in range(len(x)):
        if x[char] == "?":
            return d[len(x) - char]
        elif not d[x[char]]:
            return 0
        d = d[x[char]]
