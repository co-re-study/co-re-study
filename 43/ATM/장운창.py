input()
print(sum(v*i for i,v in enumerate(sorted(map(int,input().split()))[::-1],1)))
