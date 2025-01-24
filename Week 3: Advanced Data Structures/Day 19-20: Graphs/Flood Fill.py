from collections import deque


def floodFill(image, sr, sc, newColor):
    rows, cols = len(image), len(image[0])
    originalColor = image[sr][sc]

    # If the new color is the same as the original color, return the image as is
    if originalColor == newColor:
        return image

    queue = deque([(sr, sc)])

    while queue:
        r, c = queue.popleft()

        # Change the cell's color to the new color
        image[r][c] = newColor

        # Check the 4 neighbouring cells
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc

            # If the neighbouring cell is within bounds and has the original color
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == originalColor:
                queue.append((nr, nc))

    return image


image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
sr = 1
sc = 1
newColor = 2
print(floodFill(image, sr, sc, newColor))
