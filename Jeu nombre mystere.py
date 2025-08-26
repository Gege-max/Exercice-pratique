print("__Le jeu du nombre mystère__")

def nombre_secret(nbs):   # Définition de la fonction
    
    a = int(input("Entrez un nombre:  "))  # On demande à l'utilisateur un premier nombre
    
    # Tant que la réponse n'est pas correcte, on continue la boucle
    while a != nbs:  
        
        if a > nbs:   # Si le nombre proposé est plus grand que le secret
            print("Ce nombre est trop grand.")   
            a = int(input("Entrez un nombre: "))  # On redemande un nombre
            
        elif a < nbs:   # Si le nombre proposé est plus petit que le secret
            print("Ce nombre est trop petit.")
            a = int(input("Entrez un nombre: "))  # On redemande un nombre
    
    # Quand l'utilisateur trouve le bon nombre, on sort de la boucle et on affiche :
    else:
        print("Vous avez trouvé le bon nombre 🎉 Woupiiiiiii !")

# Appel de la fonction avec 8 comme nombre secret
nombre_secret(8)
