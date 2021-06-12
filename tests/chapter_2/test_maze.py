from classic_cs_problems.chapter_2.maze import Cell, Maze

def test_default_maze():
    maze: Maze = Maze()
    total_cells = maze._rows * maze._columns
    blocked_cells = 0
    for row in range(maze._rows):
        for column in range(maze._columns):
            if maze._grid[row][column] == Cell.BLOCKED:
                blocked_cells += 1
    assert abs(blocked_cells/total_cells - maze._sparseness) < .05



def test_non_default_maze():
    maze: Maze = Maze(rows=25, columns=25, sparseness=.5)
    total_expected_cells = maze._rows * maze._columns
    total_cells = 0
    blocked_cells = 0
    for row in range(maze._rows):
        for column in range(maze._columns):
            if maze._grid[row][column] == Cell.BLOCKED:
                blocked_cells += 1
            total_cells +=1
    assert total_cells == total_expected_cells
    assert abs(blocked_cells/total_cells - maze._sparseness) < .05