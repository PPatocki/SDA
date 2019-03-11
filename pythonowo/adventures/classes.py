from random import randint

class Class():
    def __init__(self, armour=5, *args, **kwargs):
        self.armour = armour
    def attack(self):
        return 8
    def deal_damage(self, obj):
        damage_delt = randint(0, self.attack()) - obj.character_class.armour
        if damage_delt > 0:
            obj.take_damage(damage_delt)
        

class Mage(Class):
    def __init__(self, armour=2, max_attack=15, *args, **kwargs):
        super(Mage, self).__init__(armour=armour, *args, **kwargs)
        self.max_attack = max_attack
    
    def attack(self):
        return randint(2, self.max_attack)


class Warrior(Class):
    pass

class Archer(Class):
    pass


class Thief(Class):
    def attack(self):
        critical = randint(1, 10)
        if critical > 7:
            return 10
        return 2
