import os

def main():

    # Create list of tuples for each hand of the RPS game
    lines = readfile("./day3/input.txt")
    print(lines[0])
    tup = makeTuple("ttgJtRGJQctTZtZT")

    scoringChar = ''
    for char1 in tup[0]:
        for char2 in tup[1]:
            if char1 == char2:
                scoringChar = char1
                break
                break

    print(scoringChar)


#    pairslist = []
#    for line in lines:
#        pairslist.append(tuple(line.split(" ")))

def makeTuple(line: str):
    halfLen = len(line)//2
    return (line[:halfLen], line[halfLen:])


# Read input, and split by lines
def readfile(file : str ):
    f = open(f"./{file}", "r")
    return f.read().split("\n")

if __name__ == "__main__":
    main()
