from battle import battle
from maps import total_win

class Player:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y

    def check_position(key):
        '''check next position and calls appropriate function'''
        new_x, new_y = key[0], key[1]
        if map[new_x][new_y] == '-':
            move(new_x, new_y)
        elif map[new_x][new_y] == 'M':
            battle()
        elif map[new_x][new_y] == 'x':
            print('wall lol')
        elif map[new_x][new_y] == 'E':
            total_win()

    def move(self, new_x, new_y):
        '''moves character'''
        map[new_x][new_y], map[self.x][self.y] = '@', '-' 
        self.x = new_x
        self.y = new_y 
