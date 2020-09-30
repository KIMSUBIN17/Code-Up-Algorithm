n = input()

amount = n[1] + n[0]
amount = int(amount)*2

if(amount>99):
    amount = amount % 100

if(amount<=50):
    print(amount)
    print('GOOD')
else:
    print(amount)
    print('OH MY GOD')
