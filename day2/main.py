import os
from collections import namedtuple

def main():

    # Part 1
    part1 = readfile("input.txt")
    pairslist = []
    for line in part1:
        pairslist.append(tuple(line.split(" ")))

    #print(pairslist)

    scoreAggr = 0
    scoreAggr2 = 0

    for item in pairslist:
        print(item)
        if item[0] != '':
           scoreAggr += score(item)
           scoreAggr2 += scorept2(item)
    print(f"part 1 answer is {scoreAggr} ")
    print(f"part 2 answer is {scoreAggr2} ")

    # Part 2

def scorept2(hand: tuple):
    score = 0
    if hand[1] == 'X':
        if hand[0] == 'A':
            score +=3
        elif hand[0] == 'B':
            score +=1
        elif hand[0] == 'C':
            score +=2
    elif hand[1] == 'Y':
        score += 3
        if hand[0] == 'A':
            score +=1
        elif hand[0] == 'B':
            score +=2
        elif hand[0] == 'C':
            score +=3
    elif hand[1] == 'Z':
        score += 6
        if hand[0] == 'A':
            score +=2
        elif hand[0] == 'B':
            score +=3
        elif hand[0] == 'C':
            score +=1
    return score



def score(hand: tuple):
    score = 0
    if hand[1] == 'X':
        score += 1
    elif hand [1] == 'Y':
        score += 2
    elif hand [1] == 'Z':
        score += 3

    if (hand[1] == 'X' and hand[0] == 'A' or
        hand[1] == 'Y' and hand[0] == 'B' or
        hand[1] == 'Z' and hand[0] == 'C'):
        score +=3

    if (hand[1] == 'X' and hand[0] == 'C' or
        hand[1] == 'Y' and hand[0] == 'A' or
        hand[1] == 'Z' and hand[0] == 'B'):
        score +=6

    return score

    
def readfile(file : str ):
    f = open(f"./{file}", "r")
    return f.read().split("\n")

if __name__ == "__main__":
    
    main()