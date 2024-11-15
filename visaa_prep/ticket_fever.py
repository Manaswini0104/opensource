T=int(input())
for _ in range(T):
    N,M=list(map(int,input().split()))
    if N-M>=0:
        print(N-M)
    else:
        print("0")
