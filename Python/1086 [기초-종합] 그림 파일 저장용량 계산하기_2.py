a,b,c=input().split()

W=int(a)
H=int(b)
B=int(c)

print('%.2f MB' % (W*H*B/8/1024/1024))
