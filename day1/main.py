import os

def main():
    part1 = readfile("input.txt")
    # print(part1)

    counter = 0
    listOfCalories = []
    for nums in part1:
        if nums == '':
            listOfCalories.append(counter)
            counter = 0
        else:
            counter = counter + int(nums)
    listOfCalories.sort(reverse=True)
    # Part 1 answer:
    print(f"Part 1 answer = {listOfCalories[0]}")
    # Part 2 answer:
    print(f"Part 2 answer = {listOfCalories[0]+listOfCalories[1]+listOfCalories[2]}")
    
def readfile(file : str ):
    f = open(f"./day1/{file}", "r")
    return f.read().split("\n")

if __name__ == "__main__":
    
    main()