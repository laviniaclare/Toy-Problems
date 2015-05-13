
"""Write a function that takes a matrix and examines each item in a spiral order, printing each item as it comes to it.

For example, given a matrix like this as input:

[[11, 12, 13, 14, 15],
[21, 22, 23, 24, 25],
[31, 32, 33, 34, 35],
[41, 42, 43, 44, 45]]
Your program must print:

11 12 13 14 15 25 35 45 44 43 42 41 31 21 22 23 24 34 33 32"""


def spiral(matrix):
        top_row = 0
        middle_rows = 1
        row_start = 0
        row_end = len(matrix[0]) - 1
        bottom_row = len(matrix) - 1
        while top_row < bottom_row:
                #print top row
                for item in matrix[top_row][row_start:row_end + 1]:
                        print item
                #print right most column
                for row in matrix[middle_rows:bottom_row]:
                        print row[row_end]
                #print bottom row
                for item in reversed(matrix[bottom_row][row_start:row_end + 1]):
                        print item
                #print left most column
                for row in reversed(matrix[top_row + 1:bottom_row]):
                        print row[row_start]
                top_row += 1
                middle_rows += 1
                row_end -= 1
                row_start += 1
                bottom_row -= 1


spiral([[11, 12, 13, 14, 15], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35], [41, 42, 43, 44, 45]])
