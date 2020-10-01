hour, minute = map(int,input().split())


if(minute - 30 < 0):
    minute = 60 + (minute - 30)
    if(hour - 1 < 0):
        hour = 23
    else:
        hour -= 1
else:
    minute -= 30

print(hour,minute)
