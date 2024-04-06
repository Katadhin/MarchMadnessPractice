import random
from collections import Counter

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

sweet_16_matchups = [
    ('University of Connecticut Huskies', 'San Diego State Aztecs'),
    ('Iowa State Cyclones', 'Illinois Fighting Illini'),
    ('North Carolina Tar Heels', 'Alabama Crimson Tide'),
    ('Arizona Wildcats', 'Clemson Tigers'),
    ('Houston Cougars', 'Duke Blue Devils'),
    ('Marquette Golden Eagles', 'NC State Wolfpack'),
    ('Purdue Boilermakers', 'Gonzaga Bulldogs'),
    ('Tennessee Volunteers', 'Creighton Bluejays'),

# Update to use `team_stats_with_efficiency`
def calculate_strength(team_name, upset_multiplier=1.0, round_factor=1.0):
    team = team_stats_with_efficiency[team_name]
    strength = (team['scoring_offense'] - team['scoring_defense']) + (team['assists'] / 100)
    return round(strength * round_factor * upset_multiplier, 2)

# The rest of your functions, adjusting the simulate_game and run_weighted_simulation to correct logic

def run_weighted_simulation(num_simulations=100000):
    final_four_counter = Counter()
    champion_counter = Counter()
    for _ in range(num_simulations):
        # Assume upset_factors logic and simulate_round as you've defined
        # Correcting the final round simulation logic

    # Display results
    # Adjusted to correctly output the results
