import os
import pprint

def main():

    instructions = readfile("./day5/input.txt")

    crates = list([])
    buildCrates(crates)

    part1(instructions, crates)


def part1(instructions: str, crates: list([])):
    for line in instructions:
        tup = processInstructions(line)
        i=0
        if len(crates[tup[1]-1]) < (tup[0]):
            tup[0] = len(crates[tup[1]-1])
        while i < tup[0]:
            crates[tup[2]-1].append(crates[tup[1]-1].pop())
            i +=1

    part1 = ""
    for crate in crates:
        if len(crate) > 0:
            part1 += (crate[len(crate)-1])
    print(f"Part 1 answer: {part1}")


def processInstructions(instr: str):
    if len(instr) == 18:
        moves = instr[5]
        start = instr[12]
    elif len(instr) == 19:
        moves = instr[5:7]
        start = instr[13]

    return (int(moves), int(start), int(instr[-1]))

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
