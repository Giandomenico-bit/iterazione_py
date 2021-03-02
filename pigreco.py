# PiGreco
# Si scriva un programma in Python che calcoli il valore di π mediante la formula:

# π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...
# Il numero di termini della serie da utilizzare deve essere chiesto all'utente.

# Esempio di esecuzione:

# Approssimazione di Pi Greco
# mediante la serie:

# 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

# Quanti termini vuoi utilizzare? 5
# PI: 3.33968253968

termini = input( "Inserisci numero termini : " )

termini = int( termini )
pigreco = 0.0
i = 1
count = 0
esponente = -1

while count < termini :

    if i % 2 != 0 :
        esponente = -esponente
        termine = 4.0 / float( i )
        termine = termine * esponente
        pigreco = pigreco + termine
        count = count + 1
    i = i + 1

print( pigreco )
