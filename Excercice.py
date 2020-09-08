def Maj_Min() : #en utilisant le code ascii des lettres (en decimales)
    etat = input("Entrez miniscule ou majuscule.\n")
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #la variable initiale
    if etat == 'majuscule' :
        print("Avant : ",alphabet.lower())
        print("Apres : ",end='')
        for letter in alphabet.lower() :
            letter_number = ord(letter) # ord() renvoie le valeur représentant l'unicode d'un caractère spécifié.
            letter_number = letter_number - 32
            print(chr(letter_number),end = "") # chr() renvoie l'unicode d'un caractere d'une valeur specifie
    elif etat == 'miniscule' :
         print("Avant : ",alphabet)
         print("Apres : ",end='')
         for letter in alphabet :
            letter_number = ord(letter)
            letter_number = letter_number + 32
            print(chr(letter_number),end = "")

Maj_Min()