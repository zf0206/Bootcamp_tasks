

def print_ugly(grid):
    print('[', end='')
    for row_ix, row in enumerate(grid):
        if(row_ix < len(grid)-1):
            print(row, end=',')
            print()
        else:
            print(row, end='')
    print(']')

# define a function called converter
def count_mines1(grid):
    # enumerate gives the index and element, here a list (grid is a list of lists)
    for row_ix, row_list in enumerate(grid):
        # enumerate gives the index and element, here a symbol (row is a list of symbols)
        for col_ix, element in enumerate(row_list):
            if(grid[row_ix][col_ix] == '#'): 
                continue
            min_row = 0
            min_col = 0
            max_row = len(grid)-1
            max_col = len(row_list)-1
            count = 0
            # check row above: top left, top, top right
            if(row_ix-1 >= min_row):
                if(col_ix-1 >= min_col and grid[row_ix-1][col_ix-1] == '#'):
                    count += 1
                if(grid[row_ix-1][col_ix] == '#'):
                    count += 1
                if(col_ix+1 <= max_col and grid[row_ix-1][col_ix+1] == "#"):
                    count += 1
            # check same row: left, right
            if(col_ix-1 >= min_col and grid[row_ix][col_ix-1] == '#'):
                count += 1
            if(col_ix+1 <= max_col and grid[row_ix][col_ix+1] == '#'):
                count += 1
            # check row below: bottom left, bottom, bottom right
            if(row_ix+1 <= max_row):
                if(col_ix-1 >= min_col and grid[row_ix+1][col_ix-1] == '#'):
                    count += 1
                if(grid[row_ix+1][col_ix] == '#'): count += 1
                if(col_ix+1 <= max_col and grid[row_ix+1][col_ix+1] == '#'):
                    count += 1
            # convert count into a str for required output format
            grid[row_ix][col_ix] = str(count)
    
    # print the 2D list in required format
    print('[', end='')
    for row_ix, row in enumerate(grid):
        if(row_ix < len(grid)-1):
            print(row, end=',')
            print()
        else:
            print(row, end='')
    print(']')

#grit = input ("Please enter a grit with '#' and '-':\n")
grid = [ ["-", "-", "-", "#", "#"],
         ["-", "#", "-", "-", "-"],
         ["-", "-", "#", "-", "-"],
         ["-", "#", "#", "-", "-"],
         ["-", "-", "-", "-", "-"] ]
count_mines1(grid)