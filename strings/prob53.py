## https://www.hackerrank.com/challenges/the-minion-game/problem

from itertools import combinations
def minion_game(string):
    l = len(string)
    stuart, kevin = 0,0
    for x in range(l):
        if(string[x] in 'AEIOU'): kevin+= (l-x)
        else: stuart+= (l-x)
    print("Draw") if kevin==stuart else print("Stuart {0}".format(stuart) if stuart>kevin else "Kevin {0}".format(kevin))

if __name__ == '__main__':
    s = input()
    minion_game(s)

    