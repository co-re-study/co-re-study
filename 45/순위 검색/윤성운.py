def solution(info, query):
    
    language = {"cpp": [], "java": [], "python": []}
    job = {"backend": [], "frontend": []}
    career = {"junior": [], "senior": []}
    soulfood = {"pizza": [], "chicken": []}
    
    for i in info:
        data = i.split()
        language[data[0]].append(int(data[4]))
        job[data[1]].append(int(data[4]))
        career[data[2]].append(int(data[4]))
        soulfood[data[3]].append(int(data[4]))
        
    language["cpp"].sort()
    language["java"].sort()
    language["python"].sort()
    job["backend"].sort()
    job["frontend"].sort()
    career["junior"].sort()
    career["senior"].sort()
    soulfood["pizza"].sort()
    soulfood["chicken"].sort()
        
    answer = []
        
    for q in query:
        data = q.split()
        data = [data[0], data[2], data[4], data[6], data[7]]
        total_min = 987654321
        
        max_num = 0
        if data[0] != "-" and language.get(data[0]):
            for idx in range(len(language[data[0]])):
                if language[data[0]][idx] >= int(data[4]):
                    break
            else:
                if language[data[0]][-1] < int(data[4]):
                    idx = len(language[data[0]])
            if len(language[data[0]]) - idx > max_num:
                max_num = idx
        if data[0] == "-":
            max_num = len(language[data[0]])
        if max_num < total_min:
            total_min = max_num
            
        max_num = 0
        if data[1] != "-" and job.get(data[1]):
            for idx in range(len(job[data[1]])):
                if job[data[1]][idx] >= int(data[4]):
                    break
            else:
                if job[data[1]][-1] < int(data[4]):
                    idx = len(job[data[1]])
            if len(job[data[1]]) - idx > max_num:
                max_num = idx
        if data[1] == "-":
            max_num = len(job[data[1]])
        if max_num < total_min:
            total_min = max_num
            
        
                
        answer.append(max_num)
    
    return answer