# Fonction factorielle récursive
def factorielle(n):
    """
    Calcule la factorielle n! de manière récursive.
    Vérifie que n est un entier positif ou nul.
    """
    # Vérification du type
    if not isinstance(n, int):
        return "Erreur: on doit etre un entier"
    
    # Vérification que n n'est pas négatif
    if n < 0:
        return "Erreur: n doit etre un entier positif ou nul"
    
    # Cas de base : 0! = 1 et 1! = 1
    if n == 0 or n == 1:
        return 1
    
    # Cas récursif : n! = n * (n-1)!
    return n * factorielle(n - 1)


# Fonction Fibonacci récursive
def fibonacci(n):
    """
    Calcule le n-ième nombre de Fibonacci récursivement.
    Vérifie que n est un entier positif ou nul.
    """
    # Vérification du type
    if not isinstance(n, int):
        return "Erreur: n doit etre un entier positif ou nul"
    
    # Cas de base
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Cas récursif : F(n) = F(n-1) + F(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)


# Fonction menu principal
def menu():
    """
    Menu interactif qui propose de calculer une factorielle
    ou un nombre de Fibonacci, avec gestion des erreurs de saisie.
    """
    while True:
        print("\n=== MENU ===")
        print("1 - Calculer une factorielle")
        print("2 - Calculer le n-ieme nombre de Fibonacci")
        print("3 - Quitter")

        # Demander le choix utilisateur
        try:
            choix = int(input("Entrez votre choix: "))
        except ValueError:
            print("Erreur: Entrez un nombre entier valide")
            continue

        # Option 1 : Factorielle
        if choix == 1:
            try:
                n = int(input("Entrez un entier positif: "))
                print(f"Factorielle({n}) = {factorielle(n)}")
            except ValueError:
                print("Erreur: vous devez entrer un entier")

        # Option 2 : Fibonacci
        elif choix == 2:
            try:
                n = int(input("Entrez un entier positif: "))
                print(f"Fibonacci({n}) = {fibonacci(n)}")
            except ValueError:
                print("Erreur: vous devez entrer un entier")

        # Option 3 : Quitter
        elif choix == 3:
            print("Au revoir 👋")
            break
        
        # Mauvais choix
        else:
            print("Erreur: choix invalide")


# Point d'entrée du programme
if __name__ == "__main__":
    menu()
