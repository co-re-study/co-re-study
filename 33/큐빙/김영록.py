'''
큐브를 위 아래 앞 뒤 왼 오른 순서대로
+면 한바퀴 -면 세바퀴 돌리자
돌아갈때 5면이 돌아간다
    yyy
    yyy
    yyy
    ooo
    ooo
    ooo
ggg www bbb
ggg www bbb
ggg www bbb
    rrr
    rrr
    rrr

메인면 돌리기

012
345
678

630
741
852

바깥쪽 면 돌리기 (전개도 참고)
'''
T = int(input())
for _ in range(T):
    m = int(input())
    cube = [[c]*9 for c in 'wyrogb']
    m_list = input().split()
    for face, direction in m_list:
        u, d, f, b, l, r = cube
        faces = [[u, l, f, r, b], [d, b, r, f, l], [f, u, l, d, r], [b, r, d, l, u
                                                                     ], [l, f, u, b, d], [r, d, b, u, f]]
        main, side1, side2, side3, side4 = faces['UDFBLR'.find(face)]
        for _ in range(1 if direction == '+' else 3):
            # 메인 면 돌리기
            main[0], main[1], main[2], main[3], main[5], main[6], main[7], main[8] = main[6], main[3], main[0], main[7], main[1], main[8], main[5], main[2]
            # 바깥쪽 면 돌리기
            side1[6], side1[7], side1[8], side2[0], side2[3], side2[6], side3[8], side3[5], side3[2], side4[2], side4[1], side4[0] = side2[
                0], side2[3], side2[6], side3[8], side3[5], side3[2], side4[2], side4[1], side4[0], side1[6], side1[7], side1[8]
    for i in range(3):
        print(''.join(cube[0])[i*3:i*3+3])
