
x = input()
y = x.split()
N = len(y)
s = 0

index = 0
for i in y:
    y[index] = int(i)
    s = s + int(i)
    index += 1
m = s/N

var = 0
for i in y:
    var = var + (i-m)**2
var = var/N

print(f"mean: {m} and variance:{0.1:10.2f}")
