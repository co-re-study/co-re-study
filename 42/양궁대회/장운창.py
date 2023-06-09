maxval = 0
maxanswer = []
maxdist = 0
def solution(n, info):
    mygoal = tuple(x+1 for x in info)
    leng = len(mygoal)
    def dfs(idx, op, val, arr):
        for i in (mygoal[idx], 0): 
            if i > op:
                continue
            if idx+1 == leng:
                global maxval
                global maxanswer
                global maxdist
                yourval = 0
                myanswer = arr+[i]
                myval = val+(i>0)*(10-idx)
                for j in range(leng):
                    if info[j] >= myanswer[j] and info[j]:
                        yourval += 10-j
                if myval > yourval:
                    if not maxdist or maxdist < myval-yourval:
                        maxdist = myval-yourval
                        maxval = myval
                        maxanswer = myanswer
                    elif maxdist == myval-yourval:
                        updateflag = False
                        for k in range(leng):
                            if myanswer[-1-k] > maxanswer[-1-k]:
                                updateflag = True
                                break
                            elif myanswer[-1-k] < maxanswer[-1-k]:
                                break
                        if updateflag:
                            maxdist = myval-yourval
                            maxval = myval
                            maxanswer = myanswer
                continue
            dfs(idx+1, op-i, val+(i>0)*(10-idx), arr+[i])
    dfs(0, n, 0, [])
    if maxanswer:
        if sum(maxanswer) == sum(info):
            return maxanswer
        else:
            remain = sum(info)-sum(maxanswer)
            maxanswer[-1] += remain
            return maxanswer
    else:
        return [-1]
