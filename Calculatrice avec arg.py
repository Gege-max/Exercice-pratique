def calculatrice(operation="somme", *args):
    """
    Mini calculatrice flexible.
    
    Paramètres:
        operation (str): Type d'opération à effectuer ("somme", "produit", "max").
                         Par défaut = "somme".
        *args (int/float): Nombres à utiliser pour le calcul.
    
    Retourne:
        - La somme, le produit ou le maximum des nombres selon l'opération choisie.
        - Un message d'erreur si aucun nombre n'est fourni ou si l'opération n'est pas reconnue.
    """

    # Si aucun nombre n'est fourni, on retourne un message
    if len(args) == 0:
        return "Aucun nombre fourni"
    
    # Cas 1 : addition
    if operation == "somme":
        total = 0
        for n in args:        # On parcourt tous les nombres
            total += n        # On ajoute chaque nombre au total
        return total

    # Cas 2 : multiplication
    elif operation == "produit":
        produit = 1
        for n in args:        # On parcourt tous les nombres
            produit *= n      # On multiplie les nombres entre eux
        return produit

    # Cas 3 : maximum
    elif operation == "max":
        plus_grand = args[0]  # On suppose que le premier est le plus grand
        for n in args:        # On compare avec les autres
            if n > plus_grand:
                plus_grand = n
        return plus_grand     # Retourne le plus grand trouvé

    # Si l'opération n'est pas reconnue
    else:
        return "Opération non reconnue"


# ==== Exemples d'utilisation ====
print(calculatrice("somme", 2, 4, 5, 5))     # 16
print(calculatrice("produit", 2, 3, 4))      # 24
print(calculatrice("max", 3, 4, 4))          # 4
print(calculatrice("autre", 3, 4, 45, 5))    # Opération non reconnue
print(calculatrice("somme"))                 # Aucun nombre fourni
