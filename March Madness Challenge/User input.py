import random
from collections import Counter
import math

# Provided team stats for all Sweet Sixteen teams
team_stats = {
    'North Carolina Tar Heels': {'scoring_defense': 68.5, 'scoring_offense': 82.0, 'assists': 500, 'fg_pct': 0.472, 'three_pt_pct': None, 'rebounds': 39.2, 'turnovers': 11.1, 'seed': 8, 'offensive_efficiency': 1.117},
    'Iowa State Cyclones': {'scoring_defense': 61.2, 'scoring_offense': 75.0, 'assists': 400, 'fg_pct': 0.461, 'three_pt_pct': None, 'rebounds': 36.8, 'turnovers': 10.8, 'seed': 6, 'offensive_efficiency': 1.095},
    'NC State Wolfpack': {'scoring_defense': 70.0, 'scoring_offense': 77.0, 'assists': 450, 'fg_pct': 0.455, 'three_pt_pct': 0.340, 'rebounds': 37.5, 'turnovers': 12.0, 'seed': 11, 'offensive_efficiency': 1.078},
    'Gonzaga Bulldogs': {'scoring_defense': 69.0, 'scoring_offense': 85.0, 'assists': 571, 'fg_pct': 0.490, 'three_pt_pct': 0.375, 'rebounds': 38.0, 'turnovers': 10.5, 'seed': 3, 'offensive_efficiency': 1.181},
    'Arizona Wildcats': {'scoring_defense': 64.9, 'scoring_offense': 87.6, 'assists': 651, 'fg_pct': 0.549, 'three_pt_pct': 0.373, 'rebounds': None, 'turnovers': None, 'seed': 2, 'offensive_efficiency': 1.146},
    'Illinois Fighting Illini': {'scoring_defense': 65.9, 'scoring_offense': 84.6, 'assists': 450, 'fg_pct': None, 'three_pt_pct': None, 'rebounds': None, 'turnovers': None, 'seed': 4, 'offensive_efficiency': 1.170},
    'Tennessee Volunteers': {'scoring_defense': 67.0, 'scoring_offense': 79.1, 'assists': 567, 'fg_pct': None, 'three_pt_pct': None, 'rebounds': None, 'turnovers': None, 'seed': 9, 'offensive_efficiency': 1.102},
    'Purdue Boilermakers': {'scoring_defense': 67.1, 'scoring_offense': 83.9, 'assists': 659, 'fg_pct': 0.562, 'three_pt_pct': 0.392, 'rebounds': 2054.0, 'turnovers': None, 'seed': 5, 'offensive_efficiency': 1.185},
    'Marquette Golden Eagles': {'scoring_defense': 68.0, 'scoring_offense': 80.0, 'assists': 450, 'fg_pct': 0.555, 'three_pt_pct': None, 'rebounds': 2196.0, 'turnovers': None, 'seed': 19, 'offensive_efficiency': 1.106},
    'Creighton Bluejays': {'scoring_defense': 64.0, 'scoring_offense': 80.6, 'assists': 575, 'fg_pct': 0.574, 'three_pt_pct': 0.365, 'rebounds': 2043.0, 'turnovers': None, 'seed': 6, 'offensive_efficiency': 1.142},
    'Duke Blue Devils': {'scoring_defense': 66.5, 'scoring_offense': 79.8, 'assists': 526, 'fg_pct': None, 'three_pt_pct': 0.380, 'rebounds': 2004.0, 'turnovers': None, 'seed': 22, 'offensive_efficiency': 1.159},
    'Clemson Tigers': {'scoring_defense': 65.9, 'scoring_offense': 74.0, 'assists': 450, 'fg_pct': None, 'three_pt_pct': None, 'rebounds': None, 'turnovers': None, 'seed': None, 'offensive_efficiency': 1.111},
    'Alabama Crimson Tide': {'scoring_defense': 68.0, 'scoring_offense': 82.0, 'assists': 545, 'fg_pct': 0.563, 'three_pt_pct': 0.366, 'rebounds': 2198.0, 'turnovers': None, 'seed': 12, 'offensive_efficiency': 1.183},
    'San Diego State Aztecs': {'scoring_defense': 66.2, 'scoring_offense': 75.0, 'assists': 450, 'fg_pct': None, 'three_pt_pct': None, 'rebounds': None, 'turnovers': None, 'seed': None, 'offensive_efficiency': None},
    'Houston Cougars': {'scoring_defense': 57.7, 'scoring_offense': 90.7, 'assists': 573, 'fg_pct': None, 'three_pt_pct': None, 'rebounds': None, 'turnovers': None, 'seed': None, 'offensive_efficiency': 1.114},
    'University of Connecticut Huskies': {'scoring_defense': 63.9, 'scoring_offense': 81.6, 'assists': 672, 'fg_pct': 0.572, 'three_pt_pct': None, 'rebounds': 2118.0, 'turnovers': None, 'seed': 36, 'offensive_efficiency': 1.198},
}

# Defined Sweet Sixteen matchups based on actual tournament pairings
sweet_16_matchups = [
    ('University of Connecticut Huskies', 'San Diego State Aztecs'),
    ('Iowa State Cyclones', 'Illinois Fighting Illini'),
    ('North Carolina Tar Heels', 'Alabama Crimson Tide'),
    ('Arizona Wildcats', 'Clemson Tigers'),
    ('Houston Cougars', 'Duke Blue Devils'),
    ('Marquette Golden Eagles', 'NC State Wolfpack'),
    ('Purdue Boilermakers', 'Gonzaga Bulldogs'),
    ('Tennessee Volunteers', 'Creighton Bluejays'),
]

# Adding a momentum factor to the team_stats dictionary based on recent performance
for team in team_stats:
    recent_wins = random.randint(4, 8)  # Simulating recent wins
    recent_losses = random.randint(1, 4)  # Simulating recent losses
    momentum = (recent_wins - recent_losses) / (recent_wins + recent_losses)
    team_stats[team]['momentum'] = max(0.9, min(1.1, 1 + momentum))  # Keeping momentum between 0.9 and 1.1

# User input section for adjusting factor weights
print("Enter the weights for each factor (default values in parentheses):")
off_def_balance_weight = float(input("Offensive/Defensive Balance Weight (0.35): ") or 0.35)
shooting_efficiency_weight = float(input("Shooting Efficiency Weight (0.2): ") or 0.2)
rebounding_factor_weight = float(input("Rebounding Factor Weight (0.15): ") or 0.15)
turnover_factor_weight = float(input("Turnover Factor Weight (0.15): ") or 0.15)
seed_factor_weight = float(input("Seed Factor Weight (0.15): ") or 0.15)
offensive_efficiency_factor_weight = float(input("Offensive Efficiency Factor Weight (0.03): ") or 0.03)

def calculate_strength(team_name, round_factor=1.0):
    team = team_stats[team_name]
    off_def_balance = (team['scoring_offense'] + team['assists'] / 100) - team['scoring_defense']
    shooting_efficiency = (team.get('fg_pct', 0) + team.get('three_pt_pct', 0)) / 2 if team.get('fg_pct') and team.get('three_pt_pct') else 0
    rebounding_factor = team.get('rebounds', 0) / 40 if team.get('rebounds') else 0
    turnover_factor = 20 / team['turnovers'] if team.get('turnovers') else 0
    seed_factor = (17 - team['seed']) / 16 if team.get('seed') else 0
    offensive_efficiency_factor = team['offensive_efficiency'] / 1.5 if team.get('offensive_efficiency') else 0

    x_factor = random.uniform(-round_factor, round_factor)
    momentum = team['momentum']

    strength = off_def_balance * off_def_balance_weight + shooting_efficiency * shooting_efficiency_weight + rebounding_factor * rebounding_factor_weight + turnover_factor * turnover_factor_weight + seed_factor * seed_factor_weight + offensive_efficiency_factor * offensive_efficiency_factor_weight + x_factor + momentum
    return strength

def simulate_game(team1, team2, round_factor=1.0):
    strength1 = calculate_strength(team1, round_factor)
    strength2 = calculate_strength(team2, round_factor)
    if strength1 > strength2:
        margin = strength1 - strength2
        team_stats[team1]['momentum'] += margin / 200
        return team1
    else:
        margin = strength2 - strength1
        team_stats[team2]['momentum'] += margin / 200
        return team2

def simulate_round(matchups, round_factor=1.0):
    winners = []
    for i, matchup in enumerate(matchups):
        team1, team2 = matchup
        winner = simulate_game(team1, team2, round_factor=round_factor)
        winners.append(winner)
    return winners

def run_tournament_simulation(num_simulations=1000000):
    final_four_counter = Counter()
    champion_counter = Counter()

    for _ in range(num_simulations):
        for team in team_stats:
            team_stats[team]['momentum'] = random.uniform(0.9, 1.1)

        # Simulating each round with increasing x-factor variability
        sweet_sixteen_winners = simulate_round(sweet_16_matchups, round_factor=0.8)
        elite_eight_winners = simulate_round([(sweet_sixteen_winners[i], sweet_sixteen_winners[i + 1]) for i in range(0, len(sweet_sixteen_winners), 2)], round_factor=1.2)
        final_four_winners = simulate_round([(elite_eight_winners[i], elite_eight_winners[i + 1]) for i in range(0, len(elite_eight_winners), 2)], round_factor=1.6)
        championship_game = [(final_four_winners[0], final_four_winners[1])]
        champion = simulate_round(championship_game, round_factor=2.0)[0]

        final_four_counter.update(final_four_winners)
        champion_counter[champion] += 1

    # Display results
    print("Final Four Appearances:")
    for team, appearances in final_four_counter.most_common():
        print(f"{team}: {appearances}")
    print("\nChampionship Wins:")
    for team, wins in champion_counter.most_common():
        print(f"{team}: {wins}")

run_tournament_simulation()