age = int(input())

year = 2012 - age+1 

if(year < 2000):
    year = str(year)
    print(int(year[2:4]),1)
else:
    year = str(year)
    print(int(year[2:4]),3)
