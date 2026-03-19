print("coucou le monde")
print("aurevoir")

class Gens :
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.prenom} {self.nom}.")

personne1 = Gens("Dupont", "Jean")
personne1.se_presenter()              