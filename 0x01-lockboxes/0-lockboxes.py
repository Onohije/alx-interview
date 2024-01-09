def canUnlockAll(boxes):
    if not boxes or len(boxes) == 0:
        return False

    # Initialize a set to keep track of visited boxes
    visited = set()
    visited.add(0)  # Mark the first box as visited

    # Initialize a stack to perform depth-first search
    stack = [0]

    # Perform depth-first search to check if all boxes can be opened
    while stack:
        current_box = stack.pop()

        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                stack.append(key)
                visited.add(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)

# Example usage:
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
