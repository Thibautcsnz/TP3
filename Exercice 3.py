from random import randint

i=0
r = randint(0,100)

a = int(input("entrer une valeur: "))

while a!=r:
    if a<r:
        print("plus grand")
        i = i + 1
    elif a>r:
        print("plus petit")
        i = i + 1
    a = int(input("entrer une valeur: "))

print("\nBien joué!")
print(f"Il vous a fallu {i} essais")