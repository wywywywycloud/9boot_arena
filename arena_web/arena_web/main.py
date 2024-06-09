from game_logic import create_random_things, equip_persons, battle_arena, create_random_persons
from module import *


def main():
    things = create_random_things()
    persons = create_random_persons()
    equip_persons(persons, things)

    print("Участники боя:")
    for person in persons:
        print(person.name)

    battle_arena(persons)


if __name__ == "__main__":
    main()
