def solution(routes):
    answer = 0
    points = {}
    routes.sort(key = lambda x:x[1])
    cameras = [routes[0][1]]
    
    for route in routes:
        start, end = route
        if start <= cameras[-1] <= end:
            continue
        else:
            cameras.append(end)
        
    return len(cameras)