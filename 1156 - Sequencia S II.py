a = 1
b = 1
sum = 0

for i in range(20):
    sum += a/b

    a += 2

    if b < 2:
        b += 1
    else:
        b *= 2

print("%.2f" % sum)