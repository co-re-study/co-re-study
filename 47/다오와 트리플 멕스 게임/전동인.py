n = int(input())
a = sorted(list(map(int, input().split())))

a = list(dict.fromkeys(a))

if a[0] != 0:
    print(0)
elif len(a) == 1 and a[0] == 0:
    print(1)
else:
    for i in range(len(a)):
        if i != a[i]:
            print(i + 2)
            break
    else:
        print(len(a) + 2)
