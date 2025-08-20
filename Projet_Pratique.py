# Demander a l'utilisateur d'entrer un code
nom = input(f"Entrez votre nom: ")
nombre1 = int(input(f"Entrez un nombre: "))
nombre2 = int(input(f"Entrez un autre nombre: "))

# Calcule
addition = nombre1 + nombre2
multiplication = nombre1 + nombre2
soustraction = nombre1 - nombre2
division = nombre1 / nombre2
modulo = nombre1 % nombre2

# Afficher le code
print(f"Bonjour !")
print(f"La somme est: {addition}")
print(f"La multi est : {multiplication}")
print(f"la soustra est : {soustraction}")
print(f"la div est: {division}")
print(f"le modulo est : {modulo}")