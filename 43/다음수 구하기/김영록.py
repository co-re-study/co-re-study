'''
끝에서부터 보는데 해당 수가 왼쪽에 있는 수보다 크면 이제 거기서부터 숫자 바꿔나가보자.
ex) 279134399742
399742 에서 9는 3보다 크니까 여기 있는 6개의 수로 399742보다 더 큰걸 만들자.
만들 수 있는 방법
1. 3을 제외한 [9, 9, 7, 4, 2] 를 sort 하자.
그러면 [2, 4, 7, 9, 9] 가 되는데 여기서 3보다 큰 수를 찾아보자.
그러면 4가 나올텐데 4와 3을 서로 자리를 바꾼다.
그러면 423799 로 399742 보다 큰 가장 작은수가 될 것이다.
'''

T = int(input())
for _ in range(T):
    flag = False
    A = list(map(int, input()))
    for i in range(len(A)-1, 0, -1):
        if A[i] > A[i-1]:
            A[i:] = sorted(A[i:])
            for j in range(i, len(A)):
                if A[i-1] < A[j]:
                    flag = True
                    A[i-1], A[j] = A[j], A[i-1]
                    print(''.join(map(str, A)))
                    break
            if flag:
                break
    else:
        print('BIGGEST')
