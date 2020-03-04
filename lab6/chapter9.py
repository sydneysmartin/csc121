def square(x):
    return x*x

def hypot(a, b):
    x = square(a)
    y = square(b)
    return (x + y)**.5

c = hypot(3, 4)
print(c)