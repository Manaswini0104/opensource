N=int(input())
if N>=1 and N<=12:
    if N>=3 and N<=5:
        print("Spring")
    elif N>=6 and N<=8:
        print("Summer")
    elif N>=9 and N<=11:
        print("Autumn")
    else:
        print("Winter")
else:
    print("Invalid")
