#!/usr/bin/env python3

'''
Keep track of who you trust in among us
'''

# color codes
colors = {'red':'124', 'blue':'27', 'green':'34', 'pink':'171', 'orange':'208', 'yellow':'226',
             'black':'0', 'white':'255', 'purple':'99', 'brown':'94', 'cyan':'51', 'lime':'47'}

# color abbreviations
colors_short = {'r': 'red', 'b': 'blue', 'g': 'green', 'p': 'pink', 'o': 'orange', 'y': 'yellow',
                'k': 'black', 'w': 'white', 'u': 'purple', 'n': 'brown', 'c': 'cyan', 'l': 'lime'}

# pad color strings
pad_c = max(len(x) for x in colors) + 1

# scores of players
players = dict()

def display_score():
    '''
    display the scores of players
    print color : score sorted
    '''
    for p in sorted(players, key=lambda x: players[x], reverse=True):
        print(f'\u001b[38;5;{colors[p]}m{p.ljust(pad_c)}: {str(players[p]).rjust(2)}\u001b[0m')

def display_players():
    '''display current players when adding/removing'''
    print(' | '.join(f'\u001b[38;5;{colors[p]}m\u2588\u001b[0m' for p in players))

def get_color(c):
    '''convert short color to color name'''
    if c in colors_short:
        return colors_short[c]
    return c

def hint(*args):
    '''print short colors'''
    for k, v in colors_short.items():
        print(f'{k}: {v}')

def add(*args):
    '''add player(s)'''
    if len(args) < 0:
        print('No color to add')
        return
    for c in args:
        color = get_color(c)
        if color in colors:
            if color not in players:
                players[color] = 0
                print(f'{color} added')
            else:
                print(f'{color} already in players')
        else:
            print(f'Color "{color}" not recognized')
    display_players()

def remove(*args):
    '''remove player(s)'''
    if len(args) < 0:
        print('No color to remove')
        return
    for c in args:
        color = get_color(c)
        if color in colors:
            if color in players:
                players.pop(color)
                print(f'{color} removed')
            else:
                print(f'{color} not in players')
        else:
            print(f'Color "{color}" not recognized')
    display_players()

def trust(*args):
    '''add point to player(s)'''
    if len(args) < 0:
        print('Missing color(s)')
        return
    for c in args:
        color = get_color(c)
        if color in players:
            players[color] += 1
            print(f'Trusted {color}')
        else:
            print(f'{color} not recognized')

def doubt(*args):
    '''remove point from player(s)'''
    if len(args) < 0:
        print('Missing color(s)')
        return
    for c in args:
        color = get_color(c)
        if color in players:
            players[color] -= 1
            print(f'Suspicious of {color}')
        else:
            print(f'{color} not recognized')

def quit(*args):
    '''quit'''
    exit()

# valid commands
cmds = {'a':add, 'r':remove, 't':trust, 'd':doubt, 'q':quit, 'h':hint}

def main():
    while True:
        print('> ', end='')
        s = input().split(' ')
        cmd = s[0]
        args = s[1:] if len(s) > 1 else []
        if cmd in cmds:
            cmds[cmd](*args)
        else:
            print(f'Command "{cmd}" not recognized')
            valid = ", ".join(f'({k}){v.__name__[1:]}' for k,v in cmds.items())
            print(f'Valid commands are {valid}')
        display_score()

if __name__ == '__main__':
    main()