def game_of_life(grid, iterations):
    """Run the Game of Life for a specified number of iterations."""
    for _ in range(iterations):
        grid = next_generation(grid)
    return grid
def next_generation(grid):
    """Calculate the next generation of the Game of Life."""
    new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            alive_neighbors = count_alive_neighbors(grid, i, j)
            if grid[i][j] == 1:  # Cell is currently alive
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_grid[i][j] = 0  # Cell dies
                else:
                    new_grid[i][j] = 1  # Cell stays alive
            else:  # Cell is currently dead
                if alive_neighbors == 3:
                    new_grid[i][j] = 1  # Cell becomes alive
    return new_grid
def count_alive_neighbors(grid, x, y):
    """Count the number of alive neighbors for a cell at (x, y)."""
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
            count += 1
    return count
# Example usage
initial_grid = [
    [0, 1, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 1]
]
iterations = 5
final_grid = game_of_life(initial_grid, iterations)
print("Final grid after", iterations, "iterations:")
for row in final_grid:
    print(row)
