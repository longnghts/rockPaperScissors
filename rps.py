import random
playerScore=0
cpuScore=0
scoreLimit = 3
while True: #=>  Copied the play again code from an online resource

    playerMove = input('What do you play? (rock, paper or scissors?):')
    choices = ['rock', 'paper', 'scissors']
    cpuMove = random.choice(choices)




    print(f'You chose {playerMove} and the computer chose {cpuMove}')

    if playerMove == cpuMove:
        print('It\'s a draw!')
    elif playerMove == 'scissors':
        if cpuMove == 'rock':
            print('Rock beats scissors, YOU LOSE!')
            cpuScore+= 1
            print(playerScore, cpuScore)
        else:
            print('Scissors cut paper, YOU WIN!')
            playerScore+= 1
            print(playerScore, cpuScore)
    elif playerMove == 'rock':
        if cpuMove == 'paper':
            print('Paper covers rock, YOU LOSE!')
            cpuScore+= 1
            print(playerScore, cpuScore)
        else:
            print('Rock beats scissors, YOU WIN!')
            playerScore+= 1
            print(playerScore, cpuScore)
    elif playerMove == 'paper':
        if cpuMove == 'scissors':
            print('Scissors cut paper, YOU LOSE!')
            cpuScore+= 1
            print(playerScore, cpuScore)
        else:
            print('Paper covers rock, YOU WIN!')
            playerScore+= 1
            print(playerScore, cpuScore)

    if cpuScore >= 3 or playerScore >= 3:
        play_again = input('Play again? (y/n): ')#=>  Copied the play again code from an online resource
        if play_again.lower() != "y":#=>  Copied the play again code from an online resource
            print('Game Over!')
            break#=>  Copied the play again code from an online resource
        else:
            cpuScore = 0
            playerScore = 0
