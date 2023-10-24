def solution(n, weak, dist):
    
    def perm(depth):
        nonlocal answer
        
        if depth == len(dist):
            for i in range(size):
                new_weak = weak[i: i + size]
                dist_idx = 0
                current_dist = new_weak[0] + selection[0]
                weak_idx = 0
                
                while True:
                    if new_weak[weak_idx] > current_dist:
                        dist_idx += 1
                        if dist_idx >= len(dist):
                            dist_idx = 987654320
                            break
                        current_dist = new_weak[weak_idx] + selection[dist_idx]
                    else:
                        weak_idx += 1
                        if weak_idx == size:
                            break
                        
                answer = min(answer, dist_idx + 1)
            return
        
        for i in range(len(dist)):
            if not check[i]:
                check[i] = 1
                selection[depth] = dist[i]
                perm(depth + 1)
                check[i] = 0
    
    
    size = len(weak)
    for i in range(len(weak) - 1):
        weak.append(weak[i] + n)
    
    check = [0] * len(dist)
    selection = [0] * len(dist)
    answer = 987654321
    
    perm(0)
    
    if answer == 987654321:
        return -1
    
    return answer