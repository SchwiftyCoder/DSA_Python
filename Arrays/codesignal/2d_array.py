"""
After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

Example

For

matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
the output should be
solution(matrix) = 9.

example 1

There are several haunted rooms, so we'll disregard them as well as any rooms beneath them. Thus, the answer is 1 + 5 + 1 + 2 = 9.
"""


def solution(matrix):
    """
    Calculates the sum of values in valid rooms of a matrix.

    A valid room is a column in the matrix that does not contain any zeros.
    The function iterates through each cell in the matrix and skips columns
    that have at least one zero entry. excluding the ones with a zero directly below them

    Time Complexity:
    O(n * m), where n is the number of rows in the matrix and m is the number of columns.

    Space Complexity:
    O(m), where m is the number of columns in the matrix.

    Args:
        matrix (list[list[int]]): A 2D list representing the matrix.

    Returns:
        int: The sum of values in valid rooms of the matrix.

    Example:
        >>> matrix = [
        ...     [5, 0, 9, 0],
        ...     [6, 3, 4, 6],
        ...     [0, 4, 0, 0]
        ... ]
        >>> solution(matrix)
        28
    """
    sum_of_rooms = 0
    banned_cols = set()  # used to store any of the rooms below the free rooms
    row_len = len(matrix)
    col_len = len(matrix[0])
    for row in range(row_len):
        for col in range(col_len):
            if matrix[row][col] != 0 and col not in banned_cols:
                sum_of_rooms += matrix[row][col]
            else:
                # add that column to banned columns
                banned_cols.add(col)

    print(sum_of_rooms)
    print(f"Banned columns: {banned_cols}")


matrix = [[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]]

solution(matrix)

matrix = [[1, 0, 2], [0, 3, 4], [5, 6, 7]]
solution(matrix)
