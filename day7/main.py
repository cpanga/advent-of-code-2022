def main():

    lines = readfile("./day7/input.txt")

    #print(lines)

    top_level = {}
    depth = 0
    previous_ls = 0

    low_level = {'casdas': 3213123, 'adsasdad': 13131231, 'dasdad': 313131}
    low_level2 = {'casdas': 3213123, 'adsasdad': 13131231, 'dasdad': 313131}
    mid_level ={"low_level": low_level}
    mid_level.append(low_level2)
    print(mid_level)

    #top_level['mid_level']['low_level'] = '{}'
   
#   for index, line in enumerate(lines):
#        if line[0] == $:
#            for subline in lines[previous_ls:index]:
#                # If we are moving directory out, decrease depth
#                if subline == "cd ..":
#                    depth -= 1
#                elif inumeric(subline[0])



# Read input, and split by lines
def readfile(file : str):
    f = open(f"./{file}", "r")
    return f.read().split('\n')

if __name__ == "__main__":
    main()
