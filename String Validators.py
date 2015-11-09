number = input()
alphanumeric=False
alphabet=False
digit=False
lowercase=False
uppercase=False

for i in number:
    
    if((i.isalpha())):
        alphabet=True
    if(i.isalnum()):
        alphanumeric=True
    if(i.isdigit()):
        digit=True
    if(i.islower()):
        lowercase=True
    if(i.isupper()):
        uppercase=True

print(alphanumeric)
print(alphabet)
print(digit)
print(lowercase)
print(uppercase)