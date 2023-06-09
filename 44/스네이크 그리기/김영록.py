n, m = map(int, input().split())
if n % 2 and m % 2:
    print(n*m-1)
    # 오른쪽 끝까지
    for a in range(2, m+1):
        print(1, a)
    # 올라가고 내려가는거 얼마나 반복할건지 (2씩 이동하는건 올라가고 내려가는게 2칸이니까)
    for b in range(0, m-3, 2):
        # 내려간다
        for c in range(2, n+1):
            print(c, m-b)
        # 올라간다
        for d in range(n, 1, -1):
            print(d, m-b-1)
    # 지그재그로 가기전에 밑으로 내려간다
    for e in range(2, n+1):
        print(e, 3)
    # 끝 두칸 지그재그 타고 올라온다
    for f in range(0, n-1, 2):
        print(n-f, 2)
        print(n-f, 1)
        print(n-f-1, 1)
        print(n-f-1, 2)
else:
    print(n*m)
    if n % 2:
        for a in range(1, m+1):
            print(1, a)
        for b in range(0, m, 2):
            for c in range(2, n+1):
                print(c, m-b)
            for d in range(n, 1, -1):
                print(d, m-b-1)
    else:
        for a in range(1, n+1):
            print(a, 1)
        for b in range(0, n, 2):
            for c in range(2, m+1):
                print(n-b, c)
            for d in range(m, 1, -1):
                print(n-b-1, d)