import pprint as pprint
import random



'''
Mine sweeper solver
'''

def gen_random_minefield(dimensions, num_mines):
  grid = [["-" for _ in range(dimensions)] for _ in range(dimensions)]

  for _ in range(num_mines):
      row = random.randint(0, dimensions-1)
      col = random.randint(0, dimensions-1)
      grid[row][col] = "#"
  return grid


def border_check(surrounding_directions_array):
  # Array with our final coordinates we want, after filtering out the coordinates outside of our borders.
  final_surrounding_directions_array = []

  for coordinate in surrounding_directions_array:
    # We care about the border elements (at row or column index 0 and 4)
    # The possible operations on the current position are +/-1 or +/-0.
    # So a spill over outside of our range would result in a coordinate equal to either -1 or 5. 
    if coordinate[0] == -1 or coordinate[0] == len(grid) or coordinate[1] == -1 or coordinate[1] == len(grid):
      # Therefore, we want to ignore any coordinates that have these values.
      pass
    # Append any other coordinates to the empty array, as they are within our borders.
    else:
      final_surrounding_directions_array.append(coordinate)

  return final_surrounding_directions_array


def mine_sweeper(grid):
  # For each row in the grid
  for current_row, rows in enumerate(grid):
    # For each element in the row
    for current_column, element in enumerate(rows):
      # If the element is a '#' ignore it, as we want bombs to be displayed as is.
      if element == "#":
        continue
      
      # Create 2D array of surrounding positions...
      # The first dimension represents the directions (North west, North, North east etc.,).
      # The second dimension represents the coordinates of the surrounding position (row number, column number).

      NorthWest = [current_row - 1, current_column - 1]
      North = [current_row - 1, current_column]
      NorthEast = [current_row - 1, current_column + 1]
      West = [current_row, current_column - 1]
      East = [current_row, current_column + 1]
      SouthWest = [current_row + 1, current_column - 1]
      South = [current_row + 1, current_column]
      SouthEast = [current_row + 1, current_column + 1]

      surrounding_directions_array = [NorthWest, North, NorthEast, West, East, SouthWest, South, SouthEast]
      
      # We now want to filter out any of the above surrounding positions that would result in a position outside of our borders.
      final_surrounding_directions_array = border_check(surrounding_directions_array)
      
      # Count for number of mines found surrounding the current position
      mine_count = 0
      # For each coordinate in the surrounding positions
      for coordinate in final_surrounding_directions_array:
        outside_row, outside_column = coordinate[0], coordinate[1]
        # The relevant surrounding element in the grid has the same coordinate of the position in the surrounding positions array
        outside_element = grid[outside_row][outside_column]
        # If the relevant surrounding element is '#'
        if outside_element == "#":
          # Add 1 to the mine_count
          mine_count += 1
        else:
          # Else check the next position in the surrounding positions array
          continue
      #Replace the current position, with the mine_count in the output_grid
      output_grid[current_row][current_column] = mine_count
      
  return output_grid

dimensions = random.randint(5, 10)
num_of_mines = random.randint(5, 10)

grid = gen_random_minefield(dimensions, num_of_mines)

# We will modify this copy of the grid, and use the original grid as a reference
output_grid = grid

pprint.pprint(grid)

solved_grid = mine_sweeper(grid)

pprint.pprint(solved_grid)



