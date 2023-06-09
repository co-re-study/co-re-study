for _ in range(int(input())):
    word = list(map(int,list(input())))
    worditer = -1
    for i in range(len(word)-1, -1, -1):
        if word[i] < worditer:
            worditer = i
            break
        worditer = word[i]
    if i:
        changed = word[i:]
        target = min(x for x in set(changed[1:]) if x > word[i])
        changed.remove(target)
        print(''.join(map(str,word[:i]+[target]+sorted(changed))))
    else:
        print('BIGGEST')
