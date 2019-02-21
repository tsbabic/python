from random import randint

class RPS:
    def __init__(self, name, win, lose):
        self.n = name
        self.w = win
        self.l = lose

    def get_name(self):
        return self.n

    def get_win(self):
        return self.w

    def get_lose(self):
        return self.l

rock = RPS('rock', 'scissors', 'paper')
paper = RPS('paper', 'rock', 'scissors')
scissors = RPS('scissors', 'paper', 'rock')
rps = [rock, paper, scissors]
play_game = True
print('*************')
print('welcome to rock-paper-scissors!')
print('each round is best out of three.')
print('can you beat the computer?')
print('*************')
while play_game:
    i = 1
    comp_score = 0
    user_score = 0
    while i < 4:
        pos = randint(0, 2)
        computer_choice = rps[pos]
        guess = input('enter your guess: ')
        if guess == computer_choice.get_name():
            print('you both guessed the same thing, try again.')
        elif guess == computer_choice.get_win():
            print(f'{computer_choice.get_name()} beats {guess}! one point for the computer.')
            comp_score += 1
            i += 1
        elif guess == computer_choice.get_lose():
            print(f'{guess} beats {computer_choice.get_name()}! one point for you.')
            user_score += 1
            i += 1
        else:
            print('not a valid guess, try again!')
    print('*************')
    print('Game over!')
    print('*************')
    if comp_score > user_score:
        print(f'the computer wins with {comp_score}/3 winning plays!')
    elif user_score > comp_score:
        print(f'you win with {user_score}/3 winning plays!')
    print('*************')
    print('type "exit" to exit or press enter to play the game again.')
    user_choice = input('> ')
    print('*************')
    if user_choice == 'exit':
        print('goodbye!')
        play_game = False

    

