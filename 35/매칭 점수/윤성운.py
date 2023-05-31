def solution(word, pages):
    
    urls = [] # 각 페이지의 url
    links = [[] for _ in range(len(pages))] # 각 페이지의 외부 링크들
    scores = [] # 각 페이지의 기본 점수

    for current_page in range(len(pages)):
        page = pages[current_page]
        basic_score = 0

        # 현재 페이지의 url 저장
        for i in range(len(page) - 41):
            if page[i:i+41] == '<meta property="og:url" content="https://':
                url = ""
                j = i + 41
                while True:
                    if j == len(page) or page[j] == '"':
                        break
                    url += page[j]
                    j += 1
                urls.append(url)
        
        # 기본점수 계산
        for i in range(len(page) - len(word)):
            if page[i:i+len(word)].lower() == word.lower():
                if ord(page[i + len(word)].lower()) not in range(97, 123) and ord(page[i - 1].lower()) not in range(97, 123):
                    basic_score += 1
        scores.append(basic_score)
        
        # 외부 링크 저장
        for i in range(len(page) - 17):
            if page[i:i+17] == '<a href="https://':
                link = ""
                j = i + 17
                while True:
                    if j == len(page) or page[j] == '"':
                        break
                    link += page[j]
                    j += 1
                links[current_page].append(link)
    
    parent = [[] for _ in range(len(pages))] # 각 페이지가 가리키는 외부 페이지의 인덱스
    children = [[] for _ in range(len(pages))] # 각 페이지를 가리키는 외부 페이지의 인덱스
    for page in range(len(pages)):
        for link in links[page]:
            for i in range(len(pages)):
                if urls[i] == link:
                    parent[page].append(i)
                    children[i].append(page)
    
    # 가장 높은 점수 구하기
    answer = 0
    max_score = -1
    for page in range(len(pages)):
        score = scores[page]
        for child in children[page]:
            score += scores[child] / len(links[child])
        if score > max_score:
            answer = page
            max_score = score
        
    return answer