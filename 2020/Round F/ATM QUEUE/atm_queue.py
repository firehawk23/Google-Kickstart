import math
import sys
for t in range(int(input())):    
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))
    ans=[]
    d=[]
    for i in range(n):
        d.append([arr[i],math.ceil(arr[i]/x),i])
    d.sort(key=lambda x:x[1])
    for i in d:
        ans.append(i[2]+1)
    print('Case #{}: '.format(t+1),*ans)
