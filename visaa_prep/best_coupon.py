X = int(input())
max = 100
discount = X*0.1
if discount>max:
    max=discount
print(int(X-max))
