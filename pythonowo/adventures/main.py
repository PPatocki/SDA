import sys
from races import Elf, Dwarf, Human, Orc, Halfling
from classes import Mage, Warrior, Archer, Thief

class Create_hero():
    races = (Elf, Dwarf, Human, Orc, Halfling)
    def get_race(self):
        choice = self.get_race_from_user()
        return self.races[choice - 1]
#wczesniej byly ify a tera tak

    def get_race_from_user(self):
        choice = None
        while choice is None:
            print('Wybierz rase swojej postaci.\n1: Elf\n2: Dwarf\n3: Human\n4: Orc\n5: Halfling\nChoose wisely! ')
            choice = self.get_input_from_user(6)
        return choice
#################################################################################################
    classes = (Mage, Warrior, Archer, Thief)
    def get_class(self):
        choice = self.get_class_from_user()
        return self.classes[choice - 1]

    def get_class_from_user(self):
        choice = None
        while choice is None:
            print('Wybierz klase swojej postaci.\n1: Mage\n2: Warrior\n3: Archer\n4: Thief\nChoose wisely! ')
            choice = self.get_input_from_user(5)
        return choice
#################################################################################################

    def get_input_from_user(self, limit):
        choice = None
        try:
            choice = int(input('Your choice:'))
        except ValueError:
            print('Wrong input')
        if choice not in range(1, limit):
            return None
        return choice
################################################################################################
#    @staticmethod
    def get_name(self):
        print('Choose your characters name.\nChoose wisely!')
        return input('Your characters name: ')

    def create(self):
        race = self.get_race()
        character_class = self.get_class()
        name = self.get_name()
    
        return race(name=name, character_class=character_class())


class Game():
    pass

def main():
#Create_hero.get_name() aka staticmethod
    ch = Create_hero()
    print(ch.create())
#    ch.get_race()
#    ch.get_class()    
#    ch.get_name()


if __name__ == '__main__':
    sys.exit(main())

# kiedy metoda jest statyczna mozemy z niej korzystac be tworzenia objektu
