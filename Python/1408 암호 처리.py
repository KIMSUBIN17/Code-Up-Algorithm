password = input()
encrypt1 = ''
encrypt2 = ''

for i in range(len(password)):
    asc = ord(password[i]) + 2
    encrypt1 += chr(asc)
    asc = int((ord(password[i]) * 7) % 80 + 48)
    encrypt2 += chr(asc)

print(encrypt1)
print(encrypt2)

'''
chr() : 아스키코드값 입력받아 해당하는 문자 출력
chr(97) => 'a'
ord() : 문자의 아스키코드 값을 돌려줌
ord('a') => 97
ord함수와 chr함수는 반대
'''


