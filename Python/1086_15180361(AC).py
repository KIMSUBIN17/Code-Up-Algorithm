w,h,b = map(int,input().split())

sum = w*h*b
result = sum / (8*2**20)
print("%.2f MB"%result)
