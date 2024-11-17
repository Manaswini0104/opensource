string=input()
res=[]
flag=1
for i in range(1,len(string)):
    if (string[i]==string[i-1]):
        flag+=1
    else:
        res.append(string[i-1]+str(flag))
        flag=1
res.append(string[-1]+str(flag))
output=''.join(res)
print(output)
