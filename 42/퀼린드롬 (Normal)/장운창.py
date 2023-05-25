name = list(input())
origin =   tuple('AEHIMOSTUVWXYZbdilmnopqruvwx0123578')
symmetry = tuple('A3HIMO2TUVWXY5dbilmnoqp7uvwx01SEZr8')
mdict = dict()
for i in range(len(origin)):
    mdict[origin[i]] = symmetry[i]
solo = tuple('AHIMOTUVWXYilmnouvwx018')
done = False
def mirroring(target):
    temp = ''.join(tuple(mdict[i] for i in target))
    return temp[::-1]
for i in range(len(name)):
    if name[i] in origin and name[i].lower() in origin:
        name[i] = name[i].lower()
    elif name[i].upper() in origin:
        name[i] = name[i].upper()
    elif name[i].lower() in origin:
        name[i] = name[i].lower()
    else:
        done = True
if done:
    print(-1)
else:
    answers = set()
    mirror = []
    name = ''.join(name)
    for i in name:
        if i in origin:
            mirror.append(mdict[i])
    mirror_right = ''.join(mirror)
    mirror_left = mirror_right[::-1]
    lenm = len(mirror)
    for l in range(lenm+1):
        combname = mirror_left[:l] + name
        lename = len(combname)
        mirrord = ''
        if lename%2:
            if combname[lename//2] not in solo:
                continue
            mirrord = combname[lename//2+1:]
        else:
            mirrord = combname[lename//2:]
        left = combname[:lename//2]
        right = mirroring(mirrord)
        if left == right:
            answers.add(combname)
            break
    for r in range(lenm+1):
        combname = name + mirror_right[:r][::-1]
        lename = len(combname)
        mirrord = ''
        if lename%2:
            if combname[lename//2] not in solo:
                continue
            mirrord = combname[lename//2+1:]
        else:
            mirrord = combname[lename//2:]
        left = combname[:lename//2]
        right = mirroring(mirrord)
        if left == right:
            answers.add(combname)
            break
    if answers:
        print(sorted(list(answers), key=lambda x: len(x))[0])
    else:
        print(-1)
