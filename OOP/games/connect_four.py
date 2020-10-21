"""
Connect-Four

@belovm96
"""
# attempt 3 classes
# Board
import random

class Board:
    def __init__(self):
        self.state = [[-10, -10, -10, -10],
                      [-10, -10, -10, -10],
                      [-10, -10, -10, -10],
                      [-10, -10, -10, -10]]
                      
    def check_board(self):
        diag_l_r = 0
        diag_r_l = 0
        for i in range(4):
            if sum(self.state[i]) == 4 or sum(self.state[i]) == 0:
                return False
                
            if self.state[0][i] + self.state[1][i] + self.state[2][i] + self.state[3][i] == 4 or \
                self.state[0][i] + self.state[1][i] + self.state[2][i] + self.state[3][i] == 0:
                return False
            
            diag_l_r += self.state[i][i]
            diag_r_l += self.state[4 - 1 - i][i]
        
        if diag_l_r == 4 or diag_r_l == 4 or diag_l_r == 0 or diag_r_l == 0:
            return False
        
        return True               
    
    def display(self, player1, player2):
            print('\nCurrent board state:\n', self.state[0], '\n',
                  self.state[1], '\n',
                  self.state[2], '\n',
                  self.state[3]
                  )
            print(f'\n-10 - empty\n 0 - player {player1}\n 1 - player {player2}')    
            
    def is_move_legal(self, move):
        move = int(move)
        if move < 0 or move > 3:
            print('Out of bounds!')
            return False
        
        if self.state[0][move] != -10 and self.state[1][move] != -10 and \
        self.state[2][move] != -10 and self.state[3][move] != -10:
            print('Column is full!')
            return False
        
        return True
        
    def place_move(self, player):
        move = int(player.cur_move)
        for i in range(3, -1, -1):
            if self.state[i][move] == -10:
                self.state[i][move] = player.mark
                break
                
        
        
# Player
class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        self.cur_move = None
        self.turn = False

# Game
class Game:
    def __init__(self):
        self.start = input('Welcome to Connect-Four! Please input START to start playing: ')
        if self.start == 'START':
            self.start_game()
        else:
            print('Sorry, could not start the game. Check for your input!')
            exit()
            
    def start_game(self):
        self.board = Board()
        player1_name = input('Player 1 - Please input your name: ')
        self.player1 = Player(player1_name, 0)
        player2_name = input('Player 2 - Please input your name: ')
        self.player2 = Player(player2_name, 1)
        
        print('Coin flip to figure out who plays first...')
        if random.randint(0, 1) == 0:
            self.player1.turn = True
            print(f'Player {self.player1.name} plays first')
        else:
            self.player2.turn = True
            print(f'Player {self.player2.name} plays first')
            
        self.play_game()
        
        
    def play_game(self):
        while self.board.check_board():
            if self.player1.turn == True:
                self.player = self.player1
            else:
                self.player = self.player2
                
            self.player.cur_move = input(f'Player {self.player.name} - please enter your next move (e.g. 2): ')
            
            if self.board.is_move_legal(self.player.cur_move):
                self.board.place_move(self.player)
                if self.player == self.player1:
                    self.player1.turn = False
                    self.player2.turn = True
                else:
                    self.player1.turn = True
                    self.player2.turn = False
            else:
                print('Please check your input and try again.')
                
            self.board.display(self.player1.name, self.player2.name)
            
        play_again = input(f'{self.player.name} won. Congrats! To play again, enter AGAIN: ')
        if play_again == 'AGAIN':
            self.start_game()
        else:
            exit()
                
            
game = Game()
