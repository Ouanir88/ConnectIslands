
def readFile(filename):
    ''' Opens the input file and extracts maps of islands from it.'''
    # Open the file
    file = open(filename)
    # Get the number of test cases
    T = int(file.readline())
    # List to hold maps
    grids = []
    for _ in range(T):
        # Get the map size
        line = file.readline().strip()
        R, C = line.split()
        R, C = int(R), int(C)
        # List to hold the map (will become 2-D list)
        grid = []
        # Read rows
        for _ in range(R):
            line = file.readline().strip()
            row = []
            for c in range(C):
                row.append(line[c])
            grid.append(row)
        # Add this map to the list of test cases
        grids.append(grid)
    return grids


##### Milestone 1 #####

def findLandCellsCoords(grid):
    ''' Finds and returns the list of the coordinates of the land points.'''
    landCell_list = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'X':
                landCell_list.append( (r, c) )
    return landCell_list


def coordinateToNumber(i, j, m, n):
    ''' Converts a coordinate into corresponding unique number.
        (As if counting cells on the map from left to right and from top to bottom).'''
    return i * n + j


def numberToCoordinate(t, m, n):
    ''' Converts a number back into a coordinate. Reverse of the function coordinateToNumber.'''
    j = t % n
    i = t // n
    return (i, j)


def distance(t1, t2, m, n):
    ''' Finds the distance between two cells.'''
    # Convert identity numbers into coordinates
    i1, j1 = numberToCoordinate(t1, m, n)
    i2, j2 = numberToCoordinate(t2, m, n)
    # The distance is the straight sum of differences between the coordinates
    return abs(i1 - i2) + abs(j1 - j2) - 1


def findLandCells(grid):
    ''' Returns the list of the land points.
        Each land point is represented by its unique integer.'''
    # Get the list of the land points as coordinates
    landCell_list = findLandCellsCoords(grid)
    # Convert each coordinate to its corresponding integer
    m = len(grid)
    n = len(grid[0])
    landCell_list = [coordinateToNumber(i, j, m, n) for i, j in landCell_list]
    return landCell_list



##### Driver Code #####

def main():
    # Read the input file
    filename = 'Hassan_Ouanir.txt'
    grids = readFile(filename)
    # Iterate over test cases
    for grid in grids:
        # Find the list of land cells
        landCell_list = findLandCells(grid)
        # Get the size of the grid
        m = len(grid)
        n = len(grid[0])
    print(landCell_list)

if __name__ == '__main__':
    main()


