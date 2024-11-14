v,c = input().split()
if v=="P":
    if c=="R":
        print("Vignesh")
    elif c=="S":
        print("Charan")
    else:
        print("NULL")
if v=="S":
    if c=="R":
        print("Charan")
    elif c=="P":
        print("Vignesh")
    else:
        print("NULL")
if v=="R":
    if c=="P":
        print("Charan")
    elif c=="S":
        print("Vignesh")
    else:
        print("NULL")
