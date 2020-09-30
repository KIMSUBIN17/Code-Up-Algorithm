birth, gender = input().split()
gender = int(gender)

if(gender == 1):
    year = int('19' + birth[0:2])
    print(2012 - year + 1)
elif(gender == 2):
    year = int('19' + birth[0:2])
    print(2012 - year + 1)
elif(gender == 3):
    year = int('20' + birth[0:2])
    print(2012 - year + 1)
else:
    year = int('20' + birth[0:2])
    print(2012 - year + 1)
