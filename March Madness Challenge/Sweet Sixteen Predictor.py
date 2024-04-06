import random
from collections import Counter

# Define teams with seeds, hypothetical efficiency, and x-factor
teams = {
    'Connecticut': {'seed': 1, 'off_eff': 115, 'def_eff': 90, 'x_factor': random.uniform(-3, 3), 'location_bonus': 0},
    'San Diego State': {'seed': 5, 'off_eff': 105, 'def_eff': 95, 'x_factor': random.uniform(-3, 3), 'location_bonus': 2},
    'Iowa State': {'seed': 2, 'off_eff': 110, 'def_eff': 92, 'x_factor': random.uniform(-3, 3), 'location_bonus': 1},
    'Illinois': {'seed': 3, 'off_eff': 108, 'def_eff': 93, 'x_factor': random.uniform(-3, 3), 'location_bonus': 0},
    'North Carolina': {'seed': 1, 'off_eff': 117, 'def_eff': 88, 'x_factor': random.uniform(-3, 3), 'location_bonus': 3},
    'Alabama': {'seed': 4, 'off_eff': 106, 'def_eff': 90, 'x_factor': random.uniform(-3, 3), 'location_bonus': 2},
    'Arizona': {'seed': 2, 'off_eff': 112, 'def_eff': 91, 'x_factor': random.uniform(-3, 3), 'location_bonus': 4},
    'Clemson': {'seed': 6, 'off_eff': 104, 'def_eff': 94, 'x_factor': random.uniform(-3, 3), 'location_bonus': 1},
    'Houston': {'seed': 1, 'off_eff': 116, 'def_eff': 87, 'x_factor': random.uniform(-3, 3), 'location_bonus': 2},
    'Duke': {'seed': 4, 'off_eff': 109, 'def_eff': 89, 'x_factor': random.uniform(-3, 3), 'location_bonus': 1},
    'Marquette': {'seed': 2, 'off_eff': 113, 'def_eff': 92, 'x_factor': random.uniform(-3, 3), 'location_bonus': 0},
    'NC State': {'seed': 11, 'off_eff': 103, 'def_eff': 95, 'x_factor': random.uniform(-3, 3), 'location_bonus': 2},
    'Purdue': {'seed': 1, 'off_eff': 114, 'def_eff': 89, 'x_factor': random.uniform(-3, 3), 'location_bonus': 0},
    'Gonzaga': {'seed': 5, 'off_eff': 111, 'def_eff': 93, 'x_factor': random.uniform(-3, 3), 'location_bonus': 3},
    'Tennessee': {'seed': 2, 'off_eff': 107, 'def_eff': 90, 'x_factor': random.uniform(-3, 3), 'location_bonus': 1},
    'Creighton': {'seed': 3, 'off_eff': 110, 'def_eff': 94, 'x_factor': random.uniform(-3, 3), 'location_bonus': 0},
}

def calculate_strength(team):
    # Adjust efficiency ratings based on seeding
    seed_adjustment = (16 - team['seed']) * 2
    off_eff = team['off_eff'] + seed_adjustment
    def_eff = team['def_eff'] - seed_adjustment

    # Combine offensive and defensive efficiency with the x-factor and location bonus
    return off_eff - def_eff + team['x_factor'] + team['location_bonus']

def simulate_game(team1, team2):
    strength1 = calculate_strength(teams[team1])
    strength2 = calculate_strength(teams[team2])

    # Introduce randomness in game outcome
    game_randomness = random.uniform(-5, 5)

    if strength1 + game_randomness > strength2:
        return team1
    else:
        return team2

def simulate_tournament(matchups):
    results = {}
    for matchup in matchups:
        winner = simulate_game(*matchup)
        results[winner] = results.get(winner, 0) + 1

    # If there's only one team left, it's the champion
    if len(results) == 1:
        return list(results.keys())[0]

    # Otherwise, create new matchups for the next round
    next_round_matchups = []
    for team in results:
        if results[team] > 0:
            next_round_matchups.append(team)

    next_round_matchups = list(zip(next_round_matchups[::2], next_round_matchups[1::2]))

    return simulate_tournament(next_round_matchups)

# Sweet 16 matchups
sweet_16_matchups = [
    ('Connecticut', 'San Diego State'),
    ('Iowa State', 'Illinois'),
    ('North Carolina', 'Alabama'),
    ('Arizona', 'Clemson'),
    ('Houston', 'Duke'),
    ('Marquette', 'NC State'),
    ('Purdue', 'Gonzaga'),
    ('Tennessee', 'Creighton'),
]

# Simulate the tournament many times and track the champions
num_simulations = 100000
champions = Counter()

for _ in range(num_simulations):
    champion = simulate_tournament(sweet_16_matchups)
    champions[champion] += 1

print("Tournament Simulation Results:")
for team, wins in champions.most_common():
    win_percentage = (wins / num_simulations) * 100
    print(f"{team} won {wins} times ({win_percentage:.2f}%)")
