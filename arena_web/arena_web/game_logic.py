import random
from .game_classes import *


name_list = [
    'Name 1', 'Name 2', 'Name 1', 'Name 2', 'Name 1', 'Name 2', 'Name 1', 'Name 2','Name 1', 'Name 2', 'Name 1', 'Name 2', 'Name 1', 'Name 2', 'Name 1', 'Name 2',
]


def create_random_things():
    things = []
    for i in range(10):
        thing = Thing(f"Thing {i+1}", random.uniform(0.01, 0.1),
                      random.randint(1, 10), random.randint(5, 20))
        things.append(thing)
    return sorted(things, key=lambda x: x.protection)


def create_random_persons():
    names = [f"Person {i+1}" for i in range(20)]  # Нормальные имена
    random.shuffle(names)
    persons = []
    for i in range(10):
        if random.choice([True, False]):
            person = Paladin(names[i], random.randint(50, 100), random.randint(5, 15), random.uniform(0.05, 0.15))
        else:
            person = Warrior(names[i], random.randint(50, 100), random.randint(5, 15), random.uniform(0.05, 0.15))
        persons.append(person)
    return persons


def equip_persons(persons, things):
    for person in persons:
        num_things = random.randint(1, 4)
        person.set_things(random.sample(things, num_things))


def battle_arena(persons):
    move_number = 1
    while len(persons) > 1:
        print(f"Ход {move_number}")
        attacker, defender = random.sample(persons, 2)
        damage = attacker.base_attack
        damage_taken = defender.take_damage(damage)
        print(f"{attacker.name} наносит удар по {defender.name} на {damage_taken:.2f} урона")
        
        if defender.hp <= 0:
            print(f"{defender.name} был убит!")
            persons.remove(defender)
        
        move_number += 1

    if len(persons) == 1:
        winner = persons[0]
        print(f"{winner.name} победил!!!")
