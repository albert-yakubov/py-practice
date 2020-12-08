# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# Example:
#
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:
#
# Surrounded regions shouldn’t be on the border,
# which means that any 'O' on the border
# of the board are not flipped to 'X'.
# Any 'O' that is not on the border and
# it is not connected to an 'O' on the border
# will be flipped to 'X'. Two cells are connected
# if they are adjacent cells connected horizontally or vertically.
import collections
from typing import List, Set, Tuple

def check_group(row: int, col: int, board: List[List[str]]) -> Set[Tuple[int, int]]:
    o_queue = []
    checked_spots = set([(row, col)])
    is_surrounded = True
    for (new_row, new_col) in [(row, col - 1), (row, col + 1), (row - 1, col), (row +1, col)]:
        if new_row == -1 or new_col == -1 or new_row == len(board) or new_col == len(board[new_row]):
            is_surrounded = False
            continue
        if board[new_row][new_col] == 'O' and (new_row, new_col) not in checked_spots:
            o_queue.append((new_row, new_col))
            checked_spots.add((new_row, new_col))
    while o_queue:
        (row, col) = o_queue.pop()
        for (new_row, new_col) in [(row, col - 1), (row, col + 1), (row - 1, col), (row +1, col)]:
            if new_row == -1 or new_col == -1 or new_row == len(board) or new_col == len(board[new_row]):
                is_surrounded = False
                continue
            if board[new_row][new_col] == 'O' and (new_row, new_col) not in checked_spots:
                o_queue.append((new_row, new_col))
                checked_spots.add((new_row, new_col))
    # here's where I decide to modify the 'O's
    if is_surrounded:
       for (row, col) in checked_spots:
           board[row][col] = 'X'
    return checked_spots
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        checked_spots = set([])
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 'O' and (row, col) not in checked_spots:
                    checked_spots.update(check_group(row, col, board))
        return None
# checking group is the same as checking valid
def check_group(row: int, column: int, board: List[List[str]])-> Set[Tuple[int, int]]:
    queue_of_os= []
    checked_spots = set([row, column])
    is_surrounded = True
    for new_row, new_column in [(row, column -1),(row, column + 1),(row -1, column), (row + 1, column)]:
        if new_row == -1 or new_column == -1 or new_row == len(board) or new_column == len(board[new_row]):
            is_surrounded = False
            continue
        if board[new_row][new_column] == 'O' and [new_row,new_column] not in checked_spots:
            queue_of_os.append((new_row, new_column))
            checked_spots.add((new_row, new_column))
    while queue_of_os:
        (row, column) = queue_of_os.pop()
        for (new_row, new_column) in [(row, column - 1), (row, column + 1), (row - 1, column), (row + 1, column)]:
            if new_row == -1 or new_column == -1 or new_row == len(board) or new_column == len(board[new_row]):
                is_surrounded = False
                continue
            if board[new_row][new_column] == 'O' and [new_row, new_column] not in checked_spots:
                queue_of_os.append((new_row, new_column))
                checked_spots.add((new_row, new_column))
    # here is where we decide the Os:
    if is_surrounded:
        for (row, column) in checked_spots:
            board[row][column] = "X"
    return checked_spots

def solve2(self, board: List[List[str]])->None:
    checked_spots = set([])
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 'O' and (row, column) not in checked_spots:
                checked_spots.update(check_group(row, column, board))
    return None


def is_valid(self, board, row, column):
    rows, columns = len(board), len(board[0])
    if row < 0 or column < 0 or row >= rows or column >= columns:
        return False
    return True


def solve(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    if not board or not board[0]:
        return

def bfs(self, board, row, column):
    queue = collections.deque()
    queue.append((row, column))
    board[row][column] = '#'
    while queue:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        row, column = queue.popleft()
        for direction in directions:
            next_row, next_column = row + direction[0], column + direction[1]
            if self.is_valid(board, next_row, next_column) and board[next_row][next_column] == 'O':
                queue.append((next_row, next_column))
                board[next_row][next_column] = '#'