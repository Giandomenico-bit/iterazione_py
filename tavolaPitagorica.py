# Tabelline
# Si scriva un programma in Python che stampi la tabella pitagorica.

# Esempio di output:

# 1   2   3   4   5   6   7   8   9  10
# 2   4   6   8  10  12  14  16  18  20
# 3   6   9  12  15  18  21  24  27  30
# ...

for riga in range( 1, 11 ):
    for colonna in range( 1, 11 ):
        print( riga * colonna, end=" " )
    print()
