import collections
from src import convert_input_file
import argparse


class NumIsland:
    """Find number of islands from a grid"""

    def __init__(self, grid: list[list[str]]) -> None:
        """Initialise the class

        Parameters
        ----------
        grid : list[list[str]]
            List of list depicting a grid with each position either
            0 (water) or 1 (land)
        """
        self.grid = grid
        self.total_rows = len(grid)
        self.total_cols = len(grid[0])
        self.visited = set()
        self.islands = 0
        self.directions = [
            [1, 0],
            [-1, 0],
            [0, -1],
            [0, 1],
            [1, 1],
            [1, -1],
            [-1, 1],
            [-1, -1],
        ]

    def is_valid_to_add(self, row: int, col: int) -> bool:
        """Check if a position can be added into the queue

        Parameters
        ----------
        row : int
            Number depicting row of interest
        col : int
            Number depicting column of interest

        Returns
        -------
        bool
            True if position can be added into queue
            False if position is not to be added into queue
        """
        return (
            True
            if 0 <= row < self.total_rows
            and 0 <= col < self.total_cols
            and self.grid[row][col] == "1"
            and (row, col) not in self.visited
            else False
        )

    def breadth_first_search(self, row: int, col: int):
        """Perform breadth first search on row and col of interest

        Parameters
        ----------
        row : int
            Number depicting row of interest
        col : int
            Number depicting column of interest
        """
        q = collections.deque()
        self.visited.add((row, col))
        q.append((row, col))

        while q:
            cur_row, cur_col = q.popleft()

            for row_move, col_move in self.directions:
                next_row = cur_row + row_move
                next_col = cur_col + col_move

                if self.is_valid_to_add(next_row, next_col):
                    q.append((next_row, next_col))
                    self.visited.add((next_row, next_col))

    def num_islands(self) -> int:
        """Calculate number of islands given a grid-like list of list

        Returns
        -------
        int
            number of islands in the grid
        """

        if not self.grid:
            return 0

        for row in range(self.total_rows):
            for col in range(self.total_cols):
                if self.grid[row][col] == "1" and (row, col) not in self.visited:
                    self.breadth_first_search(row, col)
                    self.islands += 1

        return self.islands


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count number of islands!")
    parser.add_argument("--input_file_path", type=str)
    args = parser.parse_args()
    grid = convert_input_file(args.input_file_path)
    counter = NumIsland(grid)
    num_of_island = counter.num_islands()
    print(num_of_island)
