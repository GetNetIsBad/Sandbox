pakket = []
kjorer = True
print("pakkeguiden 0_0")

while kjorer == True:

    meny = input("treger du å legge til noe? (pakk) eller fjerne noe? (fjern) eller vil du se hele listen? (vis) ferdig? skriv (ferdig)")

    if meny == "pakk":
        pakk = input("hva vil du legge til?")
        pakket.append(pakk)
        

    elif meny == "fjern":
        fjern = input("hva vil du fjerne?" )
        pakket.remove(fjern)
        

    elif meny == "vis":
        print(pakket)
    
    elif meny == "ferdig":
        print("da er du ferdig pakket her er lista ", pakket)
        kjorer = False

    else:
        print("det ble ikke godkjent" )
