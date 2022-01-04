#array with fruits
fruits = ["apple", "banana", "cherry"]

#initialize fruits1
fruit1 = ""
#ask user while fruit1 is not in fruits
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
