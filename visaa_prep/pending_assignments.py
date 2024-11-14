X,Y,Z = list(map(int,input().split()))
time=X*Y
deadline=Z*24*60
if time<=deadline:
    print("YES")
else:
    print("NO")
