import random 

options = ['R','P','S']

def win_condition(player1,player2):
    if player1 == player2:
        return 'Tie',0.5,0.5
    
    if player1 == 'R' and player2 == 'P':
        return 'Lose',0,1
    if player1 == 'P' and player2 == 'S':
        return 'Lose',0,1
    if player1 == 'S' and player2 == 'R':
        return 'Lose',0,1
    
    if player2 == 'R' and player1 == 'P':
        return 'Win',1,0
    if player2 == 'P' and player1 == 'S':
        return 'Win',1,0
    if player2 == 'S' and player1 == 'R':
        return 'Win',1,0

playerPoints = 0
aiPoints = 0
nos_of_game = 0
finished = False
while not finished:
    try:
        
        aiPick = random.choice(options)

        playerPick = input('Type R for Rock \n     P for Paper and \n     S for Scissors:')
        if not(playerPick in options):
            raise ValueError
        print(f'AI picks {aiPick}')
        result = win_condition(playerPick,aiPick)
        playerPoints += result[1]
        aiPoints += result[2]
        if result[0] == 'Win':
            print(f'Player wins. Points: {playerPoints} : {aiPoints}')
        if result[0] == 'Lose':
            print(f'Player lost. Points: {playerPoints} : {aiPoints}')
        if result[0] == 'Tie':
            print(f'It\'s a tie. Points: {playerPoints} : {aiPoints}')
        nos_of_game += 1
        endgame = input('Type Yes if you want to end the game, and No if you want to still continue:')
        if endgame == 'Yes':
            finished = True
        
    except ValueError:
        print(f'{playerPick} is not a valid option')
        continue


print(f'\n Summary: \n{nos_of_game} games\n{"Player" if playerPoints > aiPoints else "AI"} wins by {abs(playerPoints-aiPoints)}')