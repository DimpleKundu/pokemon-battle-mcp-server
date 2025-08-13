import random
from server.data import fetch_pokemon


# Full type effectiveness chart (Gen VI+)
TYPE_EFFECTIVENESS = {
    # Normal
    ('normal', 'rock'): 0.5, ('normal', 'ghost'): 0.0, ('normal', 'steel'): 0.5,
    # Fire
    ('fire', 'fire'): 0.5, ('fire', 'water'): 0.5, ('fire', 'grass'): 2.0, ('fire', 'ice'): 2.0,
    ('fire', 'bug'): 2.0, ('fire', 'rock'): 0.5, ('fire', 'dragon'): 0.5, ('fire', 'steel'): 2.0,
    # Water
    ('water', 'fire'): 2.0, ('water', 'water'): 0.5, ('water', 'grass'): 0.5,
    ('water', 'ground'): 2.0, ('water', 'rock'): 2.0, ('water', 'dragon'): 0.5,
    # Electric
    ('electric', 'water'): 2.0, ('electric', 'electric'): 0.5, ('electric', 'grass'): 0.5,
    ('electric', 'ground'): 0.0, ('electric', 'flying'): 2.0, ('electric', 'dragon'): 0.5,
    # Grass
    ('grass', 'fire'): 0.5, ('grass', 'water'): 2.0, ('grass', 'grass'): 0.5, ('grass', 'poison'): 0.5,
    ('grass', 'ground'): 2.0, ('grass', 'flying'): 0.5, ('grass', 'bug'): 0.5, ('grass', 'rock'): 2.0,
    ('grass', 'dragon'): 0.5, ('grass', 'steel'): 0.5,
    # Ice
    ('ice', 'fire'): 0.5, ('ice', 'water'): 0.5, ('ice', 'grass'): 2.0, ('ice', 'ice'): 0.5,
    ('ice', 'ground'): 2.0, ('ice', 'flying'): 2.0, ('ice', 'dragon'): 2.0, ('ice', 'steel'): 0.5,
    # Fighting
    ('fighting', 'normal'): 2.0, ('fighting', 'ice'): 2.0, ('fighting', 'rock'): 2.0, ('fighting', 'dark'): 2.0,
    ('fighting', 'steel'): 2.0, ('fighting', 'poison'): 0.5, ('fighting', 'flying'): 0.5,
    ('fighting', 'psychic'): 0.5, ('fighting', 'bug'): 0.5, ('fighting', 'ghost'): 0.0, ('fighting', 'fairy'): 0.5,
    # Poison
    ('poison', 'grass'): 2.0, ('poison', 'poison'): 0.5, ('poison', 'ground'): 0.5, ('poison', 'rock'): 0.5,
    ('poison', 'ghost'): 0.5, ('poison', 'steel'): 0.0, ('poison', 'fairy'): 2.0,
    # Ground
    ('ground', 'fire'): 2.0, ('ground', 'electric'): 2.0, ('ground', 'grass'): 0.5, ('ground', 'poison'): 2.0,
    ('ground', 'flying'): 0.0, ('ground', 'bug'): 0.5, ('ground', 'rock'): 2.0, ('ground', 'steel'): 2.0,
    # Flying
    ('flying', 'electric'): 0.5, ('flying', 'grass'): 2.0, ('flying', 'fighting'): 2.0,
    ('flying', 'bug'): 2.0, ('flying', 'rock'): 0.5, ('flying', 'steel'): 0.5,
    # Psychic
    ('psychic', 'fighting'): 2.0, ('psychic', 'poison'): 2.0, ('psychic', 'psychic'): 0.5,
    ('psychic', 'steel'): 0.5, ('psychic', 'dark'): 0.0,
    # Bug
    ('bug', 'grass'): 2.0, ('bug', 'psychic'): 2.0, ('bug', 'dark'): 2.0, ('bug', 'fire'): 0.5,
    ('bug', 'fighting'): 0.5, ('bug', 'poison'): 0.5, ('bug', 'flying'): 0.5, ('bug', 'ghost'): 0.5,
    ('bug', 'steel'): 0.5, ('bug', 'fairy'): 0.5,
    # Rock
    ('rock', 'fire'): 2.0, ('rock', 'ice'): 2.0, ('rock', 'flying'): 2.0, ('rock', 'bug'): 2.0,
    ('rock', 'fighting'): 0.5, ('rock', 'ground'): 0.5, ('rock', 'steel'): 0.5,
    # Ghost
    ('ghost', 'psychic'): 2.0, ('ghost', 'ghost'): 2.0, ('ghost', 'dark'): 0.5, ('ghost', 'normal'): 0.0,
    # Dragon
    ('dragon', 'dragon'): 2.0, ('dragon', 'steel'): 0.5, ('dragon', 'fairy'): 0.0,
    # Dark
    ('dark', 'psychic'): 2.0, ('dark', 'ghost'): 2.0, ('dark', 'fighting'): 0.5, ('dark', 'dark'): 0.5,
    ('dark', 'fairy'): 0.5,
    # Steel
    ('steel', 'fire'): 0.5, ('steel', 'water'): 0.5, ('steel', 'electric'): 0.5, ('steel', 'ice'): 2.0,
    ('steel', 'rock'): 2.0, ('steel', 'fairy'): 2.0, ('steel', 'steel'): 0.5,
    # Fairy
    ('fairy', 'fire'): 0.5, ('fairy', 'fighting'): 2.0, ('fairy', 'dragon'): 2.0, ('fairy', 'dark'): 2.0,
    ('fairy', 'poison'): 0.5, ('fairy', 'steel'): 0.5
}


def type_multiplier(move_type, defender_types):
    mult = 1.0
    for t in defender_types:
        mult *= TYPE_EFFECTIVENESS.get((move_type, t), 1.0)
    return mult

def calc_damage(attacker, defender, move_power, move_type, burn=False):
    atk = attacker['stats']['attack']
    defense = defender['stats']['defense']
    if burn:
        atk = atk // 2  # Burn halves physical attack
    modifier = type_multiplier(move_type, defender['types'])
    damage = (((2 * 50 / 5 + 2) * move_power * atk / defense) / 50 + 2) * modifier
    return max(1, int(damage))

def apply_status_effects(statuses, hp, log, name):
    """Apply end-of-turn effects for Burn and Poison."""
    if "burn" in statuses:
        burn_dmg = max(1, hp // 16)
        hp -= burn_dmg
        log.append(f"{name} is hurt by burn! (-{burn_dmg} HP)")
    if "poison" in statuses:
        poison_dmg = max(1, hp // 8)
        hp -= poison_dmg
        log.append(f"{name} is hurt by poison! (-{poison_dmg} HP)")
    return hp

def simulate_battle(name1, name2):
    p1 = fetch_pokemon(name1)
    p2 = fetch_pokemon(name2)
    log = []

    hp1 = p1['stats']['hp']
    hp2 = p2['stats']['hp']

    # Randomly assign one status effect to each Pokémon for demo purposes
    possible_status = [None, "burn", "poison", "paralysis"]
    status1 = random.choice(possible_status)
    status2 = random.choice(possible_status)
    statuses1 = set([status1]) if status1 else set()
    statuses2 = set([status2]) if status2 else set()

    if status1:
        log.append(f"{p1['name']} is afflicted with {status1}!")
    if status2:
        log.append(f"{p2['name']} is afflicted with {status2}!")

    turn = 1
    while hp1 > 0 and hp2 > 0:
        log.append(f"--- Turn {turn} ---")

        # Determine turn order (simple: speed stat unless paralyzed)
        speed1 = p1['stats']['speed'] // 2 if "paralysis" in statuses1 else p1['stats']['speed']
        speed2 = p2['stats']['speed'] // 2 if "paralysis" in statuses2 else p2['stats']['speed']

        if speed1 > speed2:
            first, second = (p1, hp1, statuses1), (p2, hp2, statuses2)
        else:
            first, second = (p2, hp2, statuses2), (p1, hp1, statuses1)

        # Each participant attacks if not paralyzed
        hp_first_target = None
        for attacker, attacker_hp, attacker_statuses in (first, second):
            if hp1 <= 0 or hp2 <= 0:
                break

            # Paralysis check
            if "paralysis" in attacker_statuses and random.random() < 0.25:
                log.append(f"{attacker['name']} is fully paralyzed and can't move!")
                continue

            # Decide move (using first type and 40 power for simplicity)
            if attacker is p1:
                defender = p2
                defender_hp = hp2
            else:
                defender = p1
                defender_hp = hp1

            dmg = calc_damage(attacker, defender, 40, attacker['types'][0], burn=("burn" in attacker_statuses))
            defender_hp -= dmg
            log.append(f"{attacker['name']} hits {defender['name']} for {dmg} damage! ({max(defender_hp,0)} HP left)")

            # Apply HP change
            if attacker is p1:
                hp2 = defender_hp
            else:
                hp1 = defender_hp

            if hp1 <= 0 or hp2 <= 0:
                break

        # Apply end-of-turn effects
        hp1 = apply_status_effects(statuses1, hp1, log, p1['name'])
        hp2 = apply_status_effects(statuses2, hp2, log, p2['name'])

        if hp1 <= 0 or hp2 <= 0:
            break

        turn += 1

    winner = p1['name'] if hp1 > 0 else p2['name']
    return {
        "pokemon1": p1['name'],
        "pokemon2": p2['name'],
        "winner": winner,
        "log": log
    }
