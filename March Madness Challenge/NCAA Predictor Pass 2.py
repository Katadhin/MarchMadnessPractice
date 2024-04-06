import random
from collections import Counter

# Provided team stats for all Sweet Sixteen teams
team_stats = {
    'North Carolina Tar Heels': {'scoring_defense': 68.5, 'scoring_offense': 82.0, 'assists': 500},
    'Iowa State Cyclones': {'scoring_defense': 61.2, 'scoring_offense': 75.0, 'assists': 400},
    'NC State Wolfpack': {'scoring_defense': 70.0, 'scoring_offense': 77.0, 'assists': 450},
    'Gonzaga Bulldogs': {'scoring_defense': 69.0, 'scoring_offense': 85.0, 'assists': 571},
    'Arizona Wildcats': {'scoring_defense': 64.9, 'scoring_offense': 87.6, 'assists': 651},
    'Illinois Fighting Illini': {'scoring_defense': 65.9, 'scoring_offense': 84.6, 'assists': 450},
    'Tennessee Volunteers': {'scoring_defense': 67.0, 'scoring_offense': 79.1, 'assists': 567},
    'Purdue Boilermakers': {'scoring_defense': 67.1, 'scoring_offense': 83.9, 'assists': 659},
    'Marquette Golden Eagles': {'scoring_defense': 68.0, 'scoring_offense': 80.0, 'assists': 450},
    'Creighton Bluejays': {'scoring_defense': 64.0, 'scoring_offense': 80.6, 'assists': 575},
    'Duke Blue Devils': {'scoring_defense': 66.5, 'scoring_offense': 79.8, 'assists': 526},
    'Clemson Tigers': {'scoring_defense': 65.9, 'scoring_offense': 74.0, 'assists': 450},
    'Alabama Crimson Tide': {'scoring_defense': 68.0, 'scoring_offense': 82.0, 'assists': 545},
    'San Diego State Aztecs': {'scoring_defense': 66.2, 'scoring_offense': 75.0, 'assists': 450},
    'Houston Cougars': {'scoring_defense': 57.7, 'scoring_offense': 90.7, 'assists': 573},
    'University of Connecticut Huskies': {'scoring_defense': 63.9, 'scoring_offense': 81.6, 'assists': 672},
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


# Adding a simple momentum factor to the team_stats dictionary.
# In a real scenario, this could be based on end-of-season performance or previous tournament rounds.
for team in team_stats:
    team_stats[team]['momentum'] = random.uniform(0.9, 1.1)  # Simulating momentum with a placeholder value

def calculate_strength(team_name, round_factor=1.0):
    team = team_stats[team_name]
    # Base strength calculation considers offensive and defensive efficiency, and assists.
    off_def_balance = (team['scoring_offense'] + team['assists'] / 100) - team['scoring_defense']
    # X-factor now varies more significantly in early rounds for potential upsets.
    x_factor = random.uniform(-2 * round_factor, 2 * round_factor)
    # Momentum factor influences strength based on recent performances.
    momentum = team['momentum']
    return off_def_balance + x_factor + momentum

def simulate_game(team1, team2, round_factor=1.0):
    strength1 = calculate_strength(team1, round_factor)
    strength2 = calculate_strength(team2, round_factor)
    # Determine the winner and calculate the margin of victory as a simple proxy for performance.
    if strength1 > strength2:
        margin = strength1 - strength2
        team_stats[team1]['momentum'] += margin / 100  # Adjust momentum based on performance
        return team1
    else:
        margin = strength2 - strength1
        team_stats[team2]['momentum'] += margin / 100
        return team2

def simulate_round(matchups, round_factor=1.0):
    winners = []
    for matchup in matchups:
        winner = simulate_game(matchup[0], matchup[1], round_factor)
        winners.append(winner)
    return winners

def run_tournament_simulation():
    final_four_counter = Counter()
    champion_counter = Counter()

    for _ in range(100000):
        # Resetting momentum before each simulation run for fairness
        for team in team_stats:
            team_stats[team]['momentum'] = random.uniform(0.9, 1.1)
        
        # Simulating each round with increasing x-factor variability and pressure
        elite_eight_winners = simulate_round(sweet_16_matchups, 1.0)  # Early rounds have more potential for upsets
        final_four_winners = simulate_round([(elite_eight_winners[i], elite_eight_winners[i + 1]) for i in range(0, len(elite_eight_winners), 2)], 1.2)  # Less variability
        champion = simulate_round([(final_four_winners[0], final_four_winners[1])], 1.5)[0]  # High-stakes games have the least variability

        # Update counters
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

