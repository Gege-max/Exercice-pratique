class Compte: # Class qui represente un compte bancaire
    def __init__(self, solde=0): # Constructeur avec solde initial (par defaut = 0)
        self.solde = solde # Attribut solde

    # Methode deposer
    def deposer(self, montant):
        self.solde += montant
        print(f"Vous avez ajouter {montant}. Votre compte est maintenant {self.solde}")

    # Methode retirer (verifie si le solde est suffisant)
    def retirer(self, montant): 
        if montant <= self.solde: #Verification avant retrait          
            print(f"Vous avez retirer {montant}. Votre solde est maintenant {self.solde}")
        else:
            print("Fond insuffisant")

    # Methode transfert (Verifie si le solde est insuffisant pour le transfert)
    def Transfert(self, montant, autre_compte):
        if montant <= self.solde:   #Verifiaction avant retrait
            self.solde -= montant
            autre_compte.solde += montant
            print(f"Vous avez transferé {montant} dans {autre_compte}")
        else: 
            print(f"Impossible fond insuffisant")

# Methode speciale pour afficher le code avec print
    def __str__(self):
        return f"Le solde est {self.solde}"
    
# Creation de l'objet
compte1 = Compte(500000)
compte2 = Compte(20000)

print(compte1)
print(compte2)

compte1.retirer(1000)
compte1.retirer(200)

compte1.Transfert(compte2, 30000)
compte1.Transfert(compte2, 4000)

# Utilisation de l'objet
print(compte1)
print(compte2)