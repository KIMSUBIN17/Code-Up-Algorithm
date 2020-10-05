text = input()

for i in text:
    if i.isupper():         #isupper():대문자인지 확인
        print(i.lower(),end='')
    elif i.islower():       #islower():소문자인지 확인
        print(i.upper(),end='')
    else:
        print(i,end='')
        



