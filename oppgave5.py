import random

spillere = int(input("hvor mange spillere er det? "))
teller = spillere
for i in range(spillere):
    
    print("lykke til spiller ", spillere)
    
    for i in range(3):
        kast = random.randrange(0,60)
        print(kast)
    print("du er ferdig")
    spillere = spillere - 1



    