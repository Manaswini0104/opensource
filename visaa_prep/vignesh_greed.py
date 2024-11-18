N = int(input())
arr = list(map(int,input().split()))
def maxperimeter(arr):
    arr.sort(reverse=True)
    for i in range(N-2):
        if arr[i]<arr[i+1]+arr[i+2]:
            return arr[i]+arr[i+1]+arr[i+2]
    return -1
print(maxperimeter(arr))
