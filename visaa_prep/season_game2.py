N=int(input())
if N in range(1,12):
    if N in range(3,5):
        print("Spring")
    elif N in range(6,8):
        print("Summer")
    elif N in range(9,11):
        print("Autumn")
    else:
        print("Winter")
else:
    print("Invalid")
