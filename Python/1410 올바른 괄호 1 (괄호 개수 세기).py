str = input()
openBracket = 0
closeBracket = 0

for i in range(len(str)):
    if str[i] == '(':
        openBracket += 1 
    elif str[i] == ')':
        closeBracket += 1 
        
print(openBracket,closeBracket)
