N = int(input())
k = int(input())
binary_rep=bin(N)[2:][::-1]
if k<=len(binary_rep) and binary_rep[k-1]=='1':
    print("true")
else:
    print("false")
