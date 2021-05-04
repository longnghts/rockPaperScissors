import random

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
        else:
            print('Scissors cut paper, YOU WIN!')
    elif playerMove == 'rock':
        if cpuMove == 'paper':
            print('Paper covers rock, YOU LOSE!')
        else:
            print('Rock beats scissors, YOU WIN!')
    elif playerMove == 'paper':
        if cpuMove == 'scissors':
            print('Scissors cut paper, YOU LOSE!')
        else:
            print('Paper covers rock, YOU WIN!')


    play_again = input('Play again? (y/n): ')#=>  Copied the play again code from an online resource
    if play_again.lower() != "y":#=>  Copied the play again code from an online resource
        break#=>  Copied the play again code from an online resource
