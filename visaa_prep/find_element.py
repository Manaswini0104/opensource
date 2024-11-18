N = int(input())
arr = list(map(int,input().split()))
x = int(input())
def find(arr,x):
    for i in range(N):
        if arr[i]==x:
            return i
    return -1
print(find(arr,x))
