def menu(**kwargs):
    """
    Menu simple avec kwargs.

    Paramètres:
        choix (str): "1", "2" ou "3"
        action (str): action associée (optionnel, ici juste illustratif)

    Fonctionnement:
        - Si choix = "1" → affiche "Bonjour"
        - Si choix = "2" → affiche "Au revoir"
        - Si choix = "3" → arrête le menu
        - Sinon → affiche "Choix non reconnu"
    """

    while True:  # boucle infinie, arrêtée avec break
        # Récupération des paramètres avec valeur par défaut si absent
        choix = kwargs.get("choix", "")
        action = kwargs.get("action", "")

        if choix == "1":
            print("Bonjour")
            break  # quitte la boucle après l’action

        elif choix == "2":
            print("Au revoir")
            break  # quitte la boucle après l’action

        elif choix == "3":
            print("Fin du menu")
            break  # fin du programme

        else:
            print("Choix non reconnu")
            break  # on sort aussi si la saisie est incorrecte


# ==== Exemples d'utilisation ====
menu(choix="1", action="bonjour")   # Bonjour
menu(choix="2", action="bye")       # Au revoir
menu(choix="3")                     # Fin du menu
menu(choix="9")                     # Choix non reconnu
