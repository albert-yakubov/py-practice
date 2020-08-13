'''
         3
        / \
       7   4
      /\   /\
    2    4   6
   /  \ /  \ / \
  8    5    4   3


so 3 + 7 + 4  + 9 = 23
'''
from functools import reduce
from typing import List


def _load_triangle(self, triangle_file: str) -> List[List[int]]:
    with open(triangle_file, 'r') as triangle_file:
        for triangle_row in triangle_file.readlines():
            out_row = triangle_row.strip().split()
            # or list comprehention (lines 22 and 24 do the same thing):
            # one is list comprehenssion and the other is the reducer map

            yield [int(i) for i in out_row]
            # switch from counting strings to ints
            yield list(map(lambda x: int(x), out_row))


# use the triangle as a list of lists

def max_sum(self, triangle_file: str) -> int:
    triangle_array = self._load_triangle(triangle_file)
    reduced_triangle = reduce(self._triangle_reducer, triangle_array)
    return max(reduced_triangle)


@staticmethod
def _triangle_reducer(top_row: List[int], bottom_row: List[int]) -> List[int]:
    for i, element in enumerate[bottom_row]:
        # if on first element
        if i == 0:
            bottom_row[i] = top_row[i] + element
        # if on last element
        elif i == len(bottom_row) - 1:
            bottom_row[i] = top_row[i - 1] + element
        else:
            bottom_row[i] = max(top_row[i - 1], top_row[i] + element)





# i could check this with inserted text file:
if __name__ == "__main__":
    max = max_sum(0, 'triangle.txt')
