def solution(orders, course):
    
    # 각 조합마다 몇 번 나왔는지 저장
    # comb_dict: {'AB': 1, 'AC': 4, 'BC': 2, 'ABC': 1, ...}
    comb_dict = dict()
    for order in orders:
        for i in range(1 << len(order)):
            tmp = []
            for j in range(len(order)):
                if i & (1 << j):
                    tmp.append(order[j])
            if len(tmp) > 1:
                sorted_tmp = "".join(sorted(tmp))
                if sorted_tmp in comb_dict:
                    comb_dict[sorted_tmp] += 1
                else:
                    comb_dict[sorted_tmp] = 1
    
    # cnt_max_dict: {2: 4, 3: 3, 4: 2} => 각 길이마다 가장 많이 나온 횟수 저장
    # cnt_dict: {2: ['AC'], 3: ['CDE'], 4: ['BCFG', 'ACDE']} => 각 길이마다 가장 많이 나온 조합 저장
    cnt_max_dict = dict()
    cnt_dict = dict()
    for comb in comb_dict:
        if comb_dict[comb] > 1 and len(comb) in course:
            if len(comb) in cnt_max_dict:
                if comb_dict[comb] > cnt_max_dict[len(comb)]:
                    cnt_max_dict[len(comb)] = comb_dict[comb]
                    cnt_dict[len(comb)] = [comb]
                elif comb_dict[comb] == cnt_max_dict[len(comb)]:
                    cnt_dict[len(comb)].append(comb)
            else:
                cnt_max_dict[len(comb)] = comb_dict[comb]
                cnt_dict[len(comb)] = [comb]       

    answer = []  
    for num in course:
        if num in cnt_dict:
            answer.extend(cnt_dict[num])
    answer.sort()
    
    return answer