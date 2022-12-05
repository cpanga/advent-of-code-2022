import os
import pprint

def main():

    # Create list of tuples for each hand of the RPS game
    lines = readfile("./day3/input.txt")
    
    # Part 1
    totalScore = 0
    for line in lines:
        tup = makeTuple(line)
        scoringChar = ''
        for char1 in tup[0]:
            for char2 in tup[1]:
                if char1 == char2:
                    scoringChar = char1
                    break
                    break
        if line != "":
            totalScore += score(scoringChar)    
    print(f"Part 1 answer: {totalScore}")

    # Part 2
    totalScore2 = 0
    i= 0 
    groups = []
    while i < len(lines) -1:
        tup = (lines[i],lines[i+1],lines[i+2])
        groups.append(tup)
        i +=3
    #pp = pprint.PrettyPrinter(indent=4) 
    #pp.pprint(groups)

    for group in groups:
        totalScore2 += score(findCommon(group))

    print(f"Part 2 answer: {totalScore2}")

def findCommon(group: tuple):
    for letter in group[0]:
        if letter in group[1] and letter in group[2]:
            return(letter)


def makeTuple(line: str):
    halfLen = len(line)//2
    return (line[:halfLen], line[halfLen:])

def score(charData: str):
    prio =  (ord(charData))
    if charData.isupper():
        return (prio - 38)

    if charData.islower():
        return (prio - 96)


# Read input, and split by lines
def readfile(file : str ):
    f = open(f"./{file}", "r")
    return f.read().split("\n")

if __name__ == "__main__":
    main()
