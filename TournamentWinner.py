# Tournament Winner

'''
A competition between many teams is occurring. Each duel is a 1v1 and only
one team can win a duel. A team scores 3 points for winning and 0 for losing. 

The arguments of the function are 'competitions', which is a nested array of
duels, in the form of [homeTeam, awayTeam], and 'results', which is an array
of the integers 0 and 1. 

1 = homeTeam victory
0 = awayTeam victory

The competitions and results are aligned with one another,
in terms of which teams competed in what duel
and which team won the duel. 
'''

# O(n) runtime
def tournamentWinner(competitions, results):
  # Use a dictionary to keep track of teams and their points
    team_to_point = {}
  # Zip the duel with the result
    for teams, result in zip(competitions, results):
        if (result == 1):
            # If the team is not in the dictionary, add it
            if (not (teams[0] in team_to_point)):
                team_to_point[teams[0]] = 0
            # Add 3 to winning team
            team_to_point[teams[0]] += 3
        else:
            # Same as the 2 comments above 
            if (not (teams[1] in team_to_point)):
                team_to_point[teams[1]] = 0
            team_to_point[teams[1]] += 3
    # Zip the value to the team, and then return the team with the greatest value
    return max(zip(team_to_point.values(), team_to_point.keys()))[1]
  
