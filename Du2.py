y = 1
z = int (input("zadaj cislo:"))



for x in range(1, z+1):
    if x == z: print(x)
    elif x < z: print(x, "*")
    y = y * x
    if x == z: print("=", y )



x = 1
h = 1
while x < z:
    print(x, "*")
    x = x + 1
    h = h * x
else:
    print(x)
    print("=", h)