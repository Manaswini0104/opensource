N = int(input())
arr = list(map(int,input().split()))
count=0
maximum=0
for i in range(N):
    if arr[i]==0:
        count+=1
    else:
        maximum = max(maximum,count)
        count=0
print(maximum)
