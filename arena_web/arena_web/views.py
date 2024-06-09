from django.shortcuts import render
from .game_logic import create_random_things, create_random_persons, equip_persons, battle_arena


def arena_view(request):
    things = create_random_things()
    persons = create_random_persons()
    equip_persons(persons, things)

    battle_log = ["Участники боя:"]
    for person in persons:
        battle_log.append(person.name)
    battle_log.append("")
    
    def custom_print(*args, **kwargs):
        message = " ".join(map(str, args))
        battle_log.append(message)
    
    import builtins
    original_print = builtins.print
    builtins.print = custom_print
    try:
        battle_arena(persons)
    finally:
        builtins.print = original_print

    return render(request, 'arena_web/arena.html', {'battle_log': battle_log})
