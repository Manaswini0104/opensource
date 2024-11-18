string = input()
output=""
for char in string:
    if 'A'<=char<='Z':
        output+=chr(ord(char)+32)
    elif 'a'<=char<='z':
        output+=chr(ord(char)-32)
print(output)
