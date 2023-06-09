def solution(word, pages):
    answer = 0
    word = word.lower()
    page_dict = {}
    link_dict = {}
    for i in range(len(pages)):
        pages[i] = pages[i].lower()
        page_dict[i] = {}
        page_dict[i]['link'] = []
        page = pages[i]
        page_dict[i]['counts'] = 0
        visited = [0] * len(page)
        one_word = []
        for k in range(len(page)):
            if page[k].isalpha():
                one_word.append(page[k])
            else:
                one_word = ''.join(one_word)
                if one_word == word:
                    page_dict[i]['counts'] += 1
                one_word = []
            if visited[k]:
                continue
            visited[k] = 1
            letter = page[k]
            current = []
            d = 0
            if letter == '<':  # 태그하나 모으기
                while page[k+d] != '>':
                    visited[k+d] = 1
                    current.append(page[k+d])
                    d += 1
                current.append('>')
                current = ''.join(current)
                if 'meta' in current and 'content=' in current:
                    target = current.split('"')
                    for content in target:
                        if 'https://' in content:
                            page_dict[i]['url'] = content
                            link_dict[content] = i
                if 'a href=' in current:
                    target = current.split('"')
                    for content in target:
                        if 'https://' in content:
                            page_dict[i]['link'].append(content)


    points = [0] * len(pages)
    print(link_dict)
    for i in range(len(pages)):
        page = page_dict[i]
        print(page)
        points[i] += page['counts']
        for link in page['link']:
            if link in link_dict.keys():
                target = link_dict[link]
                points[target] += page['counts'] / len(page['link'])
    for i in range(len(pages)):
        if points[i] > points[answer]:
            answer = i

    return answer

print(solution('Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n <meta charset=\"utf-8\">\n <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head> \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n <meta charset=\"utf-8\">\n <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head> \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))