#3 polia
#uzivatel zada text
#ak sa tam nachdza text, vypise v ktorom poli
#ak sa nenachadza tak zada novy text


cars = ["bmw", "audi", "skoda"]
fruits = ["apple", "banana", "cherry"]
fish = ["kapor", "stuka", "zubac"]

x = ""


while x not in fruits and x not in cars and x not in fish:
    x = input("zadaj auto, ovocie alebo rybu : ")
else:
    print(" našiel si ho")
if x in cars: print("je v skupine cars")
elif x in fruits: print("je v skupine fruits")
elif x in fish: print("je v skupine fish")
