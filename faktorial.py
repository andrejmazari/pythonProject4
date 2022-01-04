fruits = ["apple", "banana", "cherry"]

fruit1 = ""
while fruit1 not in fruits:
    fruit1 = input("zadaj ovocie: ")
else:
    print(" našiel si ho")



fruit = input("xxzadaj ovocie: ")

if fruit in fruits:
    print(fruit, " poznám")
else:
    print(fruit, " nepoznám")

for x in fruits:
    if x != "banana" and x != "cherry":
        print(x)
