from xml.etree import ElementTree
root = ElementTree.parse('dupa.xml').getroot()



for child in root:
    hp = child.attrib['hp']
    armour = child.attrib['armour']
    race = child.tag
    for gchild in child:
        if gchild.tag == 'name':
            name = gchild.text
        else:
            cls = gchild.text
    print(f'Class: {cls}, name: {name}, hp: {hp}, armour: {armour}')



'''
<heroes>
    <Orc hp="10" armour="5">
        <name>Doop'pa</name>
        <class>Warrior</class>
    </Orc>
    <Elf hp="10" armour="5">
        <name>Legolas</name>
        <class>Archer</class>
    </Elf>
    
</heroes>
'''
