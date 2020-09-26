h,b,c,s = map(int,input().split())
sum = h*b*c*s
result = sum/(8*(2**20))
print("%0.1f MB"%result)
