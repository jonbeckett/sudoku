
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]



def output():
    global grid
    output = ""
    for x in range(0,9):
        for y in range(0,9):
            output = output + str(grid[x][y]) + " "
        output = output + "\n"
    print(output)

print("\nPuzzle:\n")
output()

def possible(x,y,n):

    # use global grid
    global grid

    # loop through 0 to 8 - check coord (x,i)
    for i in range(0,9):
        if grid[x][i] == n:
            return False

    # loop through 0 to 8 - check coord (i,y)
    for i in range(0,9):
        if grid[i][y] == n:
            return False

    # use mod to work out the base coordinate of the square we are in at (x,y)
    x0 = (x//3)*3
    y0 = (y//3)*3

    # loop through the squares in the 3x3 square x,y is in, checking them
    for i in range(0,3):
        for j in range(0,3):
            if grid[x0+i][y0+j] == n:
                return False

    return True


def solve():

    # access global grid variable
    global grid

    # loop x from 0 to 8
    for x in range(9):

        # loop y from 0 to 8
        for y in range(9):

            # if grid square at x,y is empty
            if grid[x][y] == 0:

                # loop 9 times - for each digit possible (1-9)
                for n in range(1,10):

                    # check if digit is possible
                    if possible(x,y,n):

                        # if digit is possible, update global grid
                        grid[x][y] = n

                        # run the function AGAIN, having changed the number (meaning less zeros to solve)
                        solve()

                        # solve() will ALWAYS recurse if it has been able to successfully find a number
                        # - therefore, if it does not, set the number at (x,y) back to zero and wait for the backtrack (see return)
                        grid[x][y] = 0

                return
    
    # We should have a solution (if it is possible)
    print("Solution:\n")
    output()
    input("\nMore?")


solve()

