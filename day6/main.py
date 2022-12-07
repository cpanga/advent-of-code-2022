def main():

    inp = readfile("./day6/input.txt")

    print(f"part 1 solution is: {findMarker(inp,4)}")
    print(f"part 1 solution is: {findMarker(inp,14)}")

# Find where there are no duplicates in a given character range
def findMarker(inp: str, range: int):
    i = 0
    findingSolution = True
    while findingSolution:
        if (hasDuplicate(inp[i:i+range])):
            return (i+range)
            findingSolution = False
        i += 1

# Check if there are duplicate characters in a string
def hasDuplicate(string: str):
    dupes = 0
    for char in string:
        if string.count(char) != 1:
            dupes +=1
    return  dupes == 0

# Read input, and split by lines
def readfile(file : str):
    f = open(f"./{file}", "r")
    return f.read()

if __name__ == "__main__":
    main()
