t, s = map(int, input().split())

if t % 10 == 0:
    fs = s + (90 - t) / 5
else:
    fs = s + (90 - t) / 5 + 1

print(int(fs))
