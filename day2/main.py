"""
A -> Rock | X -> Rock
B -> Paper | Y -> Paper
C -> Scissors | Z -> Scissors
"""
# PART 1
with open('input.txt') as f:
    score = 0
    for round in f.read().split('\n'):
        signs = round.split(' ')
        if signs[0] == 'A' and signs[1] == 'X':
            # For choosing rock
            score += 1
            # For Draw
            score += 3
        if signs[0] == 'A' and signs[1] == 'Y':
            # For choosing paper
            score += 2
            # For winning the game
            score += 6
        if signs[0] == 'A' and signs[1] == 'Z':
            # For choosing scissiors
            score += 3
            # For losing the round
            # 0
        
        if signs[0] == 'B' and signs[1] == 'X':
            score += 1

        if signs[0] == 'B' and signs[1] == 'Y':
            score += 2
            score += 3 
        if signs[0] == 'B' and signs[1] == 'Z':
            score += 3
            score += 6

        if signs[0] == 'C' and signs[1] == 'X':
            score += 1
            score += 6

        if signs[0] == 'C' and signs[1] == 'Y':
            score += 2

        if signs[0] == 'C' and signs[1] == 'Z':
            score += 3
            score += 3
    print(score)

"""
A -> Rock | X -> Rock
B -> Paper | Y -> Paper
C -> Scissors | Z -> Scissors
"""
# PART 2
with open('input.txt') as f:
    score = 0
    for round in f.read().split('\n'):
        print(round)
        # Rock ancd Rock
        if round == 'A X':
            score += (0 + 3)
        # Rock and Paper
        if round == 'A Y':
            score += (3 + 1)
        
        if round == 'A Z':
            score += (6 +2)
        
        if round == 'B X':
            score += (1 + 0)
        if round == 'B Y':
            score += (2 + 3)
        if round == 'B Z':
            score += (3 + 6)
        
        if round == 'C X':
            score += (2 + 0)
        if round == 'C Y':
            score += (3 + 3)
        if round == 'C Z':
            score += (1 + 6)
    print(score)







