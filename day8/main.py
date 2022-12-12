def main():

    lines = readfile("./day8/input.txt")

    print("------------------------")

    y = 0
    x = 0
    visible_trees = 0
    highest_visibility = 0
    high_x = 0
    high_y = 0

    for line in lines:
        x = 0
        for tree in line:
            if is_visible(y,x,lines):
                visible_trees +=1
            if total_score(y,x,lines) > highest_visibility:
                highest_visibility = total_score(y,x,lines)
                high_x = x
                high_y = y
            x +=1 
        y +=1

    print(f"Grid is {len(lines[0])} x {len(lines)}")
    # print(f"Outer visible trees are {2*len(lines)+(2*(len(lines)-2))}")
    print(f"Total visible trees: {visible_trees}")
    print(f"Highest visibility: {highest_visibility} at y={high_y}, x={high_x}")

def total_score(y: int, x: int, lines: list) -> int:

    return (score_left(y,x,lines)*score_right(y,x,lines)*score_top(y,x,lines)*score_bot(y,x,lines))

def score_left(y: int, x: int, lines: list) -> int:

    value = int(lines[y][x])
    visibility = 0
    for tree in lines[y][:x][::-1]:
        visibility +=1
        if int(tree) >= value:
            break

    return visibility

def score_right(y: int, x: int, lines: list) -> int:

    value = int(lines[y][x])
    visibility = 0
    for tree in lines[y][x+1:]:
        visibility +=1
        if int(tree) >= value:
            break

    return visibility

def score_top(y: int, x: int, lines: list) -> int:
    value = int(lines[y][x])
    visibility = 0
    tree_list = []
    #print(f"value = {value}")
    #Get tree list:
    for line in lines[:y]:
        tree_list.append(int(line[x]))

    for tree in tree_list[::-1]:
        visibility +=1
        #print(f"tree: {tree}")
        if int(tree) >= value:
            #print(f"failed on {tree}")
            break

    return visibility

def score_bot(y: int, x: int, lines: list) -> int:
    value = int(lines[y][x])
    visibility = 0
    tree_list = []

    for line in lines[y+1:]:
        tree_list.append(int(line[x]))

    #print(tree_list)
    for tree in tree_list:
        visibility +=1
        if int(tree) >= value:
            break

    return visibility

def is_visible(y: int, x:int, lines:list) -> bool:
    return (visible_left(y,x,lines) or visible_right(y,x,lines) or visible_top(y,x,lines) or visible_bot(y,x,lines))

def visible_left(y: int, x: int, lines: list) -> bool:

   value = int(lines[y][x])
   visible = True

   for char in lines[y][:x]:
       if int(char) >= value:
           visible = False

   return visible

def visible_right(y: int, x: int, lines: list) -> bool:

   value = int(lines[y][x])
   visible = True

   for char in lines[y][x+1:]:
       if int(char) >= value:
            visible = False

   return visible

def visible_top(y: int, x: int, lines: list) -> bool:

   value = int(lines[y][x])
   visible = True

   for line in lines[:y]:
        if int(line[x]) >= value:
            visible = False

   return visible

def visible_bot(y: int, x: int, lines: list) -> bool:

   value = int(lines[y][x])
   visible = True

   for line in lines[y+1:]:
        if int(line[x]) >= value:
            visible = False

   return visible


# Read input, and split by lines
def readfile(file : str):
    f = open(f"./{file}", "r")
    return f.read().split('\n')

if __name__ == "__main__":
    main()
