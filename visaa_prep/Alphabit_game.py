s = input()
vowels = ['a','e','i','o','u','A','E','I','O','U']
vowels_count=0
cons_count=0
s=s.replace(" ","")
for char in s:
    if char.isalpha():
        if char in vowels:
            vowels_count+=1
        else:
            cons_count+=1
print(vowels_count,end=",")
print(cons_count)
