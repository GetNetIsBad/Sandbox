boker = ["The Hobbit,","Farmer Giles of Ham,","The Fellowship of the Ring,","The Two Towers,","The Return of the King,","The Adventures of Tom Bombadil,","Tree and Leaf,"]

#printer to første og to siste ved bruk av plaseringen i listen
print(boker[0],boker[1],boker[5],boker[6])

#bruker append for å legge til flere bøker
boker.append("The Simarillions,")
boker.append("Unfinished Tales")

#endrer navn på de forskjellige bøkene med kode
boker[2:3] = ["Lord of the Rings: The Fellowship of the Ring,","Lord of the Rings: The Two Towers"]
boker[4] = ["Lord of the Rings: The Return of the King,"]
#sorterer bøkene
boker.sort 
print (boker)
