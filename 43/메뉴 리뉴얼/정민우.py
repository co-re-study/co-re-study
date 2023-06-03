def solution(orders, course):
    
    subset_count_dict = {}
    
    def subset(arr):
        arr.sort()
        n = len(arr)

        for i in range(1 << n):
            now_subset = []

            for j in range(n):
                if i & (1 << j):
                    now_subset.append(arr[j])
            
            if len(now_subset) > 1:
                now_subset = tuple(now_subset)

                if now_subset in subset_count_dict:
                    subset_count_dict[now_subset] += 1
                else:
                    subset_count_dict[now_subset] = 1
    
    for order in orders:
        subset(list(order))
        
    answer = []        
    
    subset_count_list = sorted(list(subset_count_dict.items()), key=lambda x: -x[1])
    
    for course_num in course:
        max_count = 0
        for subset_count in subset_count_list:
            if subset_count[1] < 2:
                break
            if len(subset_count[0]) == course_num:
                if max_count <= subset_count[1]:
                    answer.append(''.join(subset_count[0]))
                    max_count = subset_count[1]
                else:
                    break
                    
    answer.sort()    
    
    return answer