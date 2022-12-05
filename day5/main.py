import os
import pprint

def main():

    instructions = readfile("./day5/input.txt")

    part1(instructions)
    part2(instructions)


def part2(instructions: str):
    crates = list([])
    buildCrates(crates)

    for line in instructions:
        tup = processInstructions(line)
        # Get crates to move in separate list
        i=0
        cratesToMove = []
        # If moving more crates than max number of crates, move max number instead
        if len(crates[tup[1]-1]) < (tup[0]):
            tup[0] = len(crates[tup[1]-1])
        while i < tup[0]:
            cratesToMove.append(crates[tup[1]-1].pop())
            i +=1
        cratesToMove.reverse()

        # Add crates to destination
        for item in cratesToMove:
            crates[tup[2]-1].append(item)

    print(f"Part 2 answer: {cratesOnTop(crates)}")

def part1(instructions: str):
    crates = list([])
    buildCrates(crates)
    for line in instructions:
        tup = processInstructions(line)
        i=0
        if len(crates[tup[1]-1]) < (tup[0]):
            tup[0] = len(crates[tup[1]-1])
        while i < tup[0]:
            crates[tup[2]-1].append(crates[tup[1]-1].pop())
            i +=1
    print(f"Part 1 answer: {cratesOnTop(crates)}")

# Return string of crates on top
def cratesOnTop(crates: list([])):
    topCrates = ""
    for crate in crates:
        if len(crate) > 0:
            topCrates += (crate[len(crate)-1])
    return topCrates


# Process instructions in to list of numbers
def processInstructions(instr: str):
    if len(instr) == 18:
        moves = instr[5]
        start = instr[12]
    elif len(instr) == 19:
        moves = instr[5:7]
        start = instr[13]

    return (int(moves), int(start), int(instr[-1]))

# Build the crates as shown in the problem description
def buildCrates(crates: list):
    crates.append(['R','P','C','D','B','G'])
    crates.append(['H','V','G'])
    crates.append(['N','S','Q','D','J','P','M'])
    crates.append(['P','S','L','G','D','C','N','M'])
    crates.append(['J','B','N','C','P','F','L','S'])
    crates.append(['Q','B','D','Z','V','G','T','S'])
    crates.append(['B','Z','M','H','F','T','Q'])
    crates.append(['C','M','D','B','F'])
    crates.append(['F','C','Q','G'])

# Read input, and split by lines
def readfile(file : str ):
    f = open(f"./{file}", "r")
    return f.read().split("\n")

if __name__ == "__main__":
    main()
