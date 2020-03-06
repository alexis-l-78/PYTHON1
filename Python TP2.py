class animals:
    def __init__(self,regime,nombres,nb_pattes,quantite_nourriture,domestique) :
        self.regime=regime
        self.nombres=nombres
        self.nb_pattes=nb_pattes
        self.quantite_nourriture=quantite_nourriture
        self.domestique =domestique
    def __str__(self):
        return " il y en a " + str(self.nombres) +" il est " + self.regime +" il possede " + str(self.nb_pattes)+" pattes " +" et il mange " + str(self.quantite_nourriture)

class mammifere(animals):
    pass
    def __str__(self):
        return " il y en a " + str(self.nombres) +" il est " + self.regime +" il possede" + str(self.nb_pattes)+" pattes " +" et il mange " + str(self.quantite_nourriture)
class marin(animals):
    pass
class somme:
    def __init__(self,somme):
        self.somme=somme
    def __str__(self):
        return " de nourriture a acheter par semaine est " + str(self.somme)
if __name__=="__main__":

    le_zoo={}

    le_zoo["Humain"]= animals("omnivore", 2, 2, 600, "non-domestique")
    le_zoo["Lion"]= animals("carnivore", 1, 4, 3000, "non-domestique")
    le_zoo["Lapin"]= animals("vegetarien", 7, 4, 100, "domestique")
    le_zoo["Mouton"]= animals("vegetarien", 5, 4, 500, "domestique")
    le_zoo["Chien"]= animals("omnivore", 2, 4, 500, "domestique")
    le_zoo["Pieuvre"]= animals("carnivore", 1, 0, 200, "non-domestique")
    le_zoo["Serpent"]= animals("carnivore", 2, 0, 200, "non-domestique")
    le_zoo["Autruche"]= animals("omnivore", 4, 2, 1000, "non-domestique")
    le_zoo["Poule"]= animals("omnivore", 8, 2, 200, "domestique")
    le_zoo["La_quantite"]= somme (600+3000+100+500+500+200+200+1000)
    for my_key in le_zoo:
        print(my_key+""+str(le_zoo[my_key]))
    
