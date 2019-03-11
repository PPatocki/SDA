from classes import Class
class Creature():
    def __init__(self, hp=1, *args, **kwargs):
        self.hp=hp
        self.alive = True
        character_class = kwargs.get('character_class')
        if character_class:
            self.character_class = character_class
        else:
            self.character_class = Class()
    def __str__(self):
        return f'Creature({self.hp})'
    
    def take_damage(self, damage):
        if self.hp <= damage:
            self.alive = False
        self.hp -= damage
        
class Humanoid(Creature):
    def __init__(self, name, hp=10, *args, **kwargs):
        super(Humanoid, self).__init__(hp=hp, *args, **kwargs)
        self.name = name
        
    def __str__(self):
        return f'{type(self).__name__} ({self.hp}): {self.name}'


class Elf(Humanoid):
    pass

class Dwarf(Humanoid):
    pass

class Human(Humanoid):
    pass

class Orc(Humanoid):
    pass

class Halfling(Humanoid):
    pass
