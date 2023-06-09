파수, 치킨수 = map(int,input().split())
파 = tuple(int(input()) for _ in range(파수))
시작, 끝 = 0, 1000000001
정답 = lambda x: sum(파)-x*치킨수
while 시작 < 끝-1:
    피벗 = (시작+끝)//2
    치킨카운트 = 치킨수
    for pa in 파:
        while pa >= 피벗 and 치킨카운트:
            pa -= 피벗
            치킨카운트 -= 1
        if not 치킨카운트:
            break
    if 치킨카운트:
        끝 = 피벗
    else:
        시작 = 피벗
print(정답(시작))
