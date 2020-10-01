year,month = map(int, input().split())
feb = 0

if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
    feb = 29
else:
    feb = 28

if(month < 8):
    if(month == 2):
        print(feb)
    elif(month % 2 == 0):
        print('30')
    else:
        print('31')
else:
    if(month % 2 == 0):
        print('31')
    else:
        print('30')

