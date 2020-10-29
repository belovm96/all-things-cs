"""
Minesweeper
@belovm96
"""
import string
import re
import numpy as np
import time
words = string.ascii_lowercase


class Board:
    def __init__(self, n_grid=None):
        if n_grid == None:
            n_grid = 9
        self.n_grid = n_grid
        self.cur = [[' ' for _ in range(self.n_grid)] for _ in range(self.n_grid)]


    def __repr__(self):
        # structured print for the board
        res = ''
        for i in range(2*(self.n_grid+1)):
            if i == 0:
                res += ' ' * 6
                res += '   '.join(words[:self.n_grid])
                res += ' ' * 2
                res += '\n'
                continue
            if i % 2 == 1:
                res += ' ' * 4  + '-'* (4*self.n_grid+1) + '\n'
                continue
            res += str(i//2) + ' '*(4-len(str(i//2))) + '| ' + ' | '.join(self.cur[(i-1)//2]) + ' |\n'
        return res



class Game(Board):
    def __init__(self, n_mines=None, n_grid=None):
        if n_mines is None:
            n_mines = 10
        if n_grid is None:
            n_grid = 9
        self.mine_map = Board(n_grid) # mine board
        self.dis_map = Board(n_grid) # display board
        self.n_mines = n_mines
        self.n_grid = n_grid
        self.pos_mines = list(map(lambda x: divmod(x, self.n_grid), np.random.choice(self.n_grid**2, self.n_mines, replace=False)))
        self.let_to_num = {words[i]:i for i in range(self.n_grid)}
        self.check_pos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        self.explored = {}
        self.flagged = []
        
        
    def explore(self, r, c):
        n_bombs = 0
        if (r,c) not in self.explored:
            self.explored[(r,c)] = 'e'
            for pos in self.check_pos:
                cur_r, cur_c = r + pos[0], c + pos[1]
                if cur_r >= 0 and cur_r < self.n_grid and cur_c >= 0 and cur_c < self.n_grid:
                    if (cur_r, cur_c) in self.pos_mines:
                        n_bombs += 1
            
            self.dis_map.cur[r][c] = str(n_bombs)
            
            if n_bombs != 0:
                return 0
            else:
                for pos in self.check_pos:
                    cur_r, cur_c = r + pos[0], c + pos[1]
                    if cur_r >= 0 and cur_r < self.n_grid and cur_c >= 0 and cur_c < self.n_grid:
                        self.explore(cur_r, cur_c)
        else:
            return 0
                

    def play(self):
        print('='*70)
        print("Starting Minesweeper (with {} mines on {}x{} grid.)".format(self.n_mines, self.n_grid, self.n_grid) + '\n')
        print(self.dis_map)
        print('='*70)
        self.winning = True
        
        while self.winning and not (len(self.explored) == self.n_grid**2 and sorted(self.flagged) == sorted(self.pos_mines)):
            move = input('Enter your move - a5. To flag - a5f. To unflag a5u: ')
            if len(move) == 2:
                c, r = int(self.let_to_num[move[0]]), int(move[1]) - 1
                if (r, c) in self.pos_mines:
                    print('\nYou lost!')
                    for row, col in self.pos_mines:
                        self.dis_map.cur[row][col] = '*'
                        self.winning = False
                else:
                    self.explore(r, c)
                    
            elif len(move) == 3 and move[2] == 'f':
                c, r, f = int(self.let_to_num[move[0]]), int(move[1]) - 1, move[2]
                self.flagged.append((r,c))
                self.explored[(r,c)] = f
                self.dis_map.cur[r][c] = f
                
            elif len(move) == 3 and move[2] == 'u':
                c, r, u = int(self.let_to_num[move[0]]), int(move[1]) - 1, move[2]
                self.flagged.remove((r,c))
                self.explored.pop((r,c), None)
                self.dis_map.cur[r][c] = ' '
                    
            print(self.dis_map)

    
g = Game(10, 9)
g.play()

