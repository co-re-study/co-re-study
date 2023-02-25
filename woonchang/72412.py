def solution(info, query):
    answer = []
    datas = dict()
    for lang in ("cpp", "java", "python", "-"):
        for part in ("backend", "frontend", "-"):
            for grade in ("junior", "senior", "-"):
                for food in ("chicken", "pizza", "-"):
                    datas[lang+part+grade+food] = sorted(list(int(j.split()[-1]) for j in info if (lang == "-" or lang in j) and (part == "-" or part in j) and (grade == "-" or grade in j) and (food == "-" or food in j)))
    for i in query:
        lang, part, grade, foodpoints = i.split(" and ")
        food, points = foodpoints.split()
        points = int(points)
        target = datas[lang+part+grade+food]
        start, mid, end = 0, 0, len(target)-1
        while start <= end:
            mid = (start+end)//2
            if (mid==0 and target[mid] == points) or (mid>0 and points<=target[mid] and target[mid-1]<points):
                break
            elif target[mid] < points:
                start = mid + 1
            else:
                end = mid - 1
        if start > mid:
            mid = start
        answer.append(len(target)-mid)
    return answer
