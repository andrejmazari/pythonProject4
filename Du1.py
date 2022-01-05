#3 polia
#uzivatel zada text
#ak sa tam nachdza text, vypise v ktorom poli
#ak sa nenachadza tak zada novy text

x = ""
z = x
y = x

cars = ["bmw", "audi", "skoda"]
fruits = ["apple", "banana", "cherry"]
fish = ["kapor", "stuka", "zubac"]

while x not in fruits:
    x = input("zadaj ovocie: ")
else:
    print(" našiel si ho")


while z not in cars:
    z = input("zadaj znacku auta: ")
else:
    print(" našiel si ho")

while y not in fish:
    y = input("traf nazov  ryby: ")
else:
    print(" trafil si ")

