"""
Tic-Tac-Toe

@belovm96
"""
import random 

class Player:
    def __init__(self, mark_type):
        self.mark_type = mark_type
        self.cur_move = None
        

class Board:
    def __init__(self):
        self.state = [[-10, -10, -10], 
                      [-10, -10, -10], 
                      [-10, -10, -10]]
        
    def validate(self, mark_type):
        for i in range(3):
            if sum(self.state[i]) == 3 or sum(self.state[i]) == 0 or \
            self.state[0][i]+self.state[1][i]+self.state[2][i] == 3 or \
            self.state[0][i]+self.state[1][i]+self.state[2][i] == 0:
                print(f'\nPlayer {mark_type} won!')
                return False
                
        
        if self.state[0][0]+self.state[1][1]+self.state[2][2] == 3 or  \
            self.state[0][2]+self.state[1][1]+self.state[2][0] == 3 or \
            self.state[0][0]+self.state[1][1]+self.state[2][2] == 0 or \
            self.state[0][2]+self.state[1][1]+self.state[2][0] == 0:
                print(f'\nPlayer {mark_type} won!')
                return False
            
        if self.state[0].count(-10)+self.state[1].count(-10)+self.state[2].count(-10) == 0:
            print(f'\nPlayer {mark_type} won!')
            return False
            
        return True
    
    def display(self):
        print('Current board state:\n', self.state[0], '\n',
              self.state[1], '\n',
              self.state[2])
        print('\n-10 - empty\n 0 - player O\n 1 - player X')
        
    
class Game:
    def __init__(self):
        self.start = input('Welcome to Tic-Tac_toe! To start/renew a game use enter START: ')
        if self.start == 'START':
            self.start_game()
        
    def start_game(self):
        self.board = Board()
        player_type = input('Please enter either X or O as your mark of choice: ')
        self.player1 = Player(player_type)
        if player_type == 'X':
            self.player2 = Player('O')
        else:
            self.player2 = Player('X')
            
        print(f'You are Player {self.player1.mark_type}!')
        
        print('Coin flip to figure out who plays first...')
        if random.randint(0, 1) == 0:
            self.player1.cur_move = True
            self.player = self.player1
            print(f'Player {self.player1.mark_type} plays first')
        else:
            self.player2.cur_move = True
            self.player = self.player2
            print(f'Player {self.player2.mark_type} plays first')
            
        self.make_move()
        
    def make_move(self):
        isCoord = True
        while self.board.validate(self.player.mark_type):
            if self.player1.cur_move == True and isCoord == True:
                self.player = self.player1
                self.player2.cur_move = True
            else:
                self.player = self.player2
                self.player1.cur_move = True
                
            self.player.cur_move = input(f'Player {self.player.mark_type} - please enter the coordinates of your next move (e.g 1,2): ')
            
            r, c = self.player.cur_move.split(',')
            
            if int(r) < 3 and int(c) < 3 and self.board.state[int(r)][int(c)] == -10:
                if self.player.mark_type == 'O':
                    self.board.state[int(r)][int(c)] = 0
                    
                elif self.player.mark_type == 'X':
                    self.board.state[int(r)][int(c)] = 1
                isCoord = True
                
            else:
                print('Please check your input coordinates and try again.')
                isCoord = False
                
            self.print_board()
            
    def print_board(self):
        self.board.display()
            
game = Game()
    
    