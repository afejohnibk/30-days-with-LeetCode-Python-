def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    def dfs(r, c):
        # Base case: If out of bounds or water, stop recursion
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
            return
        # Mark the cell as visited
        grid[r][c] = "0"
        # Explore all 4 possible directions
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":  # Found an unvisited island
                island_count += 1
                dfs(r, c)

    return island_count


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

print(numIslands(grid))
