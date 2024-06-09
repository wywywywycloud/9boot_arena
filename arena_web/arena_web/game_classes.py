class Thing:
    def __init__(self, name, protection, attack, health):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.health = health


class Person:
    def __init__(self, name, hp, base_attack, base_protection):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_protection = base_protection
        self.things = []

    def set_things(self, things):
        self.things = things

    def calculate_final_protection(self):
        total_protection = self.base_protection
        for thing in self.things:
            total_protection += thing.protection
        return total_protection

    def take_damage(self, attack_damage):
        final_protection = self.calculate_final_protection()
        damage_taken = max(0, attack_damage - (attack_damage
                                               * final_protection))
        self.hp -= damage_taken
        return damage_taken


class Paladin(Person):
    def __init__(self, name, hp, base_attack, base_protection):
        super().__init__(name, hp * 2, base_attack, base_protection * 2)


class Warrior(Person):
    def __init__(self, name, hp, base_attack, base_protection):
        super().__init__(name, hp, base_attack * 2, base_protection)
