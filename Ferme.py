import json
import datetime

class animal:
    def __init__(self, types, birth_year, sex):
        self.types = types
        self.birth_year = birth_year
        self.sex = sex
    def __str__(self):
        return "l'animal est " + self.types + " né le " + str(self.birth_year) + " et de sexe " + self.sex


class ferme:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def __str__(self):
        return "Ma ferme s'appelle " + self.name + " crée le " + str(self.date)
        


if __name__=="__main__":

    datetime= datetime.datetime.now()

    ferme_list = [] 
    animal_list1=[animal("une chèvre",datetime.datetime(2020,11,22),"femmelle")]
    animal_list2=[animal("un chien",datetime.datetime(2020,10,30),"mâle")]
    animal_list3=[animal("un cheval",datetime.datetime(2020,3,2),"femmelle")]

    ferme_list.append(ferme("La Ferme",datetime.datetime(2020,12,23),animal_list1))
    ferme_list.append(ferme("Ma Ferme",datetime.datetime(2020,12,23),animal_list2))
    ferme_list.append(ferme("Ta Ferme",datetime.datetime(2020,12,23),animal_list3))

   while date_time.month<12:
       date_time = date_time + datetime.timedelta(weeks=4)
       for ferme in ferme_list:
           print(ferme)
           for animal in ferme.animal_list:
               print(animal)


