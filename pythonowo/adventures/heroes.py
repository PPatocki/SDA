from classes import Mage, Warrior, Archer, Thief
from races import Elf, Orc, Halfling

class ElfWarrior:
    pass

elf_1 = Elf(name='Legolas', character_class = Warrior())
orc_1 = Orc(name="Doop'pa", hp=20, character_class = Mage())
halfling_1 = Halfling(name='Dildo Waggins')


i=1
while orc_1.alive and elf_1.alive:
    elf_1.character_class.deal_damage(orc_1)
    orc_1.character_class.deal_damage(elf_1)
    print(orc_1)
    print(elf_1)
    print(f'Round{i}')
    i += 1
