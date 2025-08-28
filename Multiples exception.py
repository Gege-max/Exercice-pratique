def operation(a, b):
    """
    Effectue la division a / b en gérant les erreurs possibles.

    Exceptions gérées :
    - ZeroDivisionError : si b = 0
    - TypeError : si a ou b ne sont pas des nombres compatibles
    """
    try:
        resultat = a / b  # tentative de division
        return resultat

    except ZeroDivisionError:
        return "Erreur : division par zéro interdite ❌"

    except TypeError:
        return "Erreur : les valeurs doivent être des nombres ❌"


# ==== Tests ====
print(operation(2, 4))       # 0.5
print(operation(2, 0))       # Erreur : division par zéro interdite ❌
print(operation("jdjdj", 9)) # Erreur : les valeurs doivent être des nombres ❌
