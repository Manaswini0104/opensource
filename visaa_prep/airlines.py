X,N=list(map(int,input().split()))
req=(N/100)
if req-int(req)>0:
    req+=1
print(int(req-X))
