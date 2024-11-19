N = int(input())
A = list(map(int,input().split()))
B = []
total_sum=sum(A)
left_wt=0
for i in range(N):
    right_wt = total_sum - left_wt-A[i]
    B.append(abs(left_wt-right_wt))
    left_wt+=A[i]
print(" ".join(map(str,B)))
