import os

def main():

    # Create list of tuples for each hand of the RPS game
    lines = readfile("./day4/input.txt")

    totalDupes = 0
    anyDupes = 0
    for line in lines:
        rangeTot = acquireRange(line)
        rangeA = list(range(int(rangeTot[0][0]),int(rangeTot[0][1])+1))
        rangeB = list(range(int(rangeTot[1][0]),int(rangeTot[1][1])+1))
        
        print(rangeA)
        print(rangeB)
        # Check if rangeA is contained in rangeB
        dupesA = 0
        for num in rangeA:
            if num in rangeB:
                dupesA += 1

        # Check if rangeB is contained in rangeA
        dupesB = 0
        for num in rangeB:
            if num in rangeA:
                dupesB += 1

        # Part 1 
        if dupesA == len(rangeA) or dupesB == len(rangeB):
            totalDupes +=1
        # Part 2
        if dupesA > 0 or dupesB > 0:
            anyDupes +=1

    print(totalDupes)
    print(anyDupes)

def acquireRange(line: str):
    split = line.split(',')
    return split[0].split('-'),split[1].split('-')

# Read input, and split by lines
def readfile(file : str ):
    f = open(f"./{file}", "r")
    return f.read().split("\n")

if __name__ == "__main__":
    main()
