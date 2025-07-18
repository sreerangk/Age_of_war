from itertools import permutations


# Battle Logic Functions

def parse_platoons(platoon_string):
    platoons = []
    for platoon in platoon_string.split(';'):
        unit_class, count = platoon.split('#')
        platoons.append((unit_class, int(count)))
    return platoons

def get_unit_advantages():
    return {
        'Militia': ['Spearmen', 'LightCavalry'],
        'Spearmen': ['LightCavalry', 'HeavyCavalry'],
        'LightCavalry': ['FootArcher', 'CavalryArcher'],
        'HeavyCavalry': ['Militia', 'FootArcher', 'LightCavalry'],
        'CavalryArcher': ['Spearmen', 'HeavyCavalry'],
        'FootArcher': ['Militia', 'CavalryArcher']
    }

def calculate_effective_strength(my_class, my_count, opponent_class, opponent_count):
    advantages = get_unit_advantages()
    
    if opponent_class in advantages[my_class]:
        effective_strength = my_count * 2
    else:
        effective_strength = my_count
    
    if effective_strength > opponent_count:
        return "Win"
    elif effective_strength == opponent_count:
        return "Draw"
    else:
        return "Loss"

def evaluate_arrangement(my_platoons, opponent_platoons):
    wins = 0
    results = []
    
    for i in range(5):
        my_class, my_count = my_platoons[i]
        opp_class, opp_count = opponent_platoons[i]
        
        result = calculate_effective_strength(my_class, my_count, opp_class, opp_count)
        results.append(result)
        
        if result == "Win":
            wins += 1
    
    return wins, results

def find_winning_arrangement(my_platoons, opponent_platoons):
    for arrangement in permutations(my_platoons):
        wins, results = evaluate_arrangement(arrangement, opponent_platoons)
        
        if wins >= 3:
            return arrangement, wins, results
    
    return None, 0, []

def format_output(arrangement):
    return ';'.join([f"{unit_class}#{count}" for unit_class, count in arrangement])

def solve_battle_problem(my_platoons_str, opponent_platoons_str):
    try:
        my_platoons = parse_platoons(my_platoons_str)
        opponent_platoons = parse_platoons(opponent_platoons_str)
        
        winning_arrangement, wins, results = find_winning_arrangement(my_platoons, opponent_platoons)
        
        if winning_arrangement is None:
            return "There is no chance of winning"
        else:
            return format_output(winning_arrangement)
    except Exception as e:
        return f"Error: {str(e)}"

def get_detailed_analysis(my_platoons_str, opponent_platoons_str):
    try:
        my_platoons = parse_platoons(my_platoons_str)
        opponent_platoons = parse_platoons(opponent_platoons_str)
        
        winning_arrangement, wins, results = find_winning_arrangement(my_platoons, opponent_platoons)
        
        if winning_arrangement is None:
            return {"error": "There is no chance of winning"}
        
        battles = []
        for i in range(5):
            my_class, my_count = winning_arrangement[i]
            opp_class, opp_count = opponent_platoons[i]
            result = results[i]
            
            battles.append({
                'battle_num': i + 1,
                'my_unit': f"{my_class}#{my_count}",
                'opponent_unit': f"{opp_class}#{opp_count}",
                'result': result
            })
        
        return {
            'arrangement': format_output(winning_arrangement),
            'wins': wins,
            'battles': battles
        }
    except Exception as e:
        return {"error": str(e)}