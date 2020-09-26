a,m,d,n=input().split()

A=int(a)
M=int(m)
D=int(d)
N=int(n)

for i in range(N-1) :
    A = A*M+D

print(A)
