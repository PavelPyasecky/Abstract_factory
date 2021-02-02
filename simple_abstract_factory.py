import yaml


hero_yaml = '''
--- !Character
factory:
    !factory assassin
name:
    7Nagibator7
'''


class HeroFactory:
    @classmethod
    def create_hero(Class, name):
        return Class.Hero(name)

    @classmethod
    def create_weapon(Class):
        return Class.Weapon()

    @classmethod
    def create_spell(Class):
        return Class.Spell()


class WariorFactory(HeroFactory):
    class Hero:
        def __init__(self, name):
            self.name = name
            self.weapon = None
            self.armor = None
            self.spell = None

        def add_weapon(self, weapon):
            self.weapon = weapon

        def add_spell(self, spell):
            self.spell = spell

        def hit(self):
            print(f"Warior hits with {self.weapon.hit()}")
            self.weapon.hit()

        def cast(self):
            print(f"Warior casts {self.spell.cast()}")
            self.spell.cast()

    class Weapon:
        def hit(self):
            return "Claymore"

    class Spell:
        def cast(self):
            return "Power"


def factory_constructor(loader, node):
    data = loader.construct_scalar(node)
    if data == "assassin":
        return AssassinFactory()
    if data == "mage":
        return MageFactory()
    else:
        return WariorFactory()



class Character(yaml.YAMLObject):
    yaml_tag = "!Character"

    def create_hero(self):
        hero = self.factory.create_hero(self.name)
        weapon = self.factory.create_weapon()
        spell = self.factory.create_spell()

        hero.add_weapon(weapon)
        hero.add_spell(spell)

        return hero


if __name__ == '__main__':
    loader = yaml.Loader
    loader.add_constructor("!factory", factory_constructor())

    hero = yaml.load(hero_yaml).create_hero()

    hero.hit()
    hero.cast()
