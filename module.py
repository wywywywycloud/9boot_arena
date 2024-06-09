class Thing:
    def __init__(self, name, protection, attack, health):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.health = health

    def add_things(self, name, hp, protection, attack, health):
        



class Person:
    def __init__(self, name, hp, base_attack, base_protection):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_protection = base_protection
        self.things = []

        





"""
import random

# Заглушки для классов "Вещи" и "Персонажи"
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
        damage_taken = max(0, attack_damage - (attack_damage * final_protection))
        self.hp -= damage_taken
        return damage_taken

class Paladin(Person):
    def __init__(self, name, hp, base_attack, base_protection):
        super().__init__(name, hp * 2, base_attack, base_protection * 2)

class Warrior(Person):
    def __init__(self, name, hp, base_attack, base_protection):
        super().__init__(name, hp, base_attack * 2, base_protection)

# Заглушка для создания произвольных вещей
def create_random_things():
    things = []
    for i in range(10):
        thing = Thing(f"Thing {i+1}", random.uniform(0.01, 0.1), random.randint(1, 10), random.randint(5, 20))
        things.append(thing)
    return sorted(things, key=lambda x: x.protection)

# Заглушка для создания персонажей
def create_random_persons():
    names = [f"Person {i+1}" for i in range(20)]
    random.shuffle(names)
    persons = []
    for i in range(10):
        if random.choice([True, False]):
            person = Paladin(names[i], random.randint(50, 100), random.randint(5, 15), random.uniform(0.05, 0.15))
        else:
            person = Warrior(names[i], random.randint(50, 100), random.randint(5, 15), random.uniform(0.05, 0.15))
        persons.append(person)
    return persons

# Одеваем персонажей рандомными вещами
def equip_persons(persons, things):
    for person in persons:
        num_things = random.randint(1, 4)
        person.set_things(random.sample(things, num_things))

# Алгоритм проведения боя
def battle_arena(persons):
    while len(persons) > 1:
        attacker, defender = random.sample(persons, 2)
        damage = attacker.base_attack
        damage_taken = defender.take_damage(damage)
        print(f"{attacker.name} наносит удар по {defender.name} на {damage_taken:.2f} урона")
        
        if defender.hp <= 0:
            print(f"{defender.name} был убит!")
            persons.remove(defender)

# Основная функция игры
def main():
    things = create_random_things()
    persons = create_random_persons()
    equip_persons(persons, things)
    battle_arena(persons)

if __name__ == "__main__":
    main()

    """