def getRow(self, rowIndex: int) -> List[int]:
    # The brute force method would be to simply generate the entire tree up to the rowIndex that was passed into the function and return the resulting rowIndex layer.
    # this will be the least efficient way but it will be the easiest to reason about.

    # the initial pascal triangle values up to level two
    pascal_triangle = [[1], [1,1]]

    # edge cases where if the rowIndex is either level one or two return those specific indexes.
    if rowIndex == 0:
        return pascal_triangle[0]
    if rowIndex == 1:
        return pascal_triangle[1]

    rowCount = 2

    while rowCount <= rowIndex:
        new_triangle_row = [1] * (rowCount + 1)
        for j_index in range(1, len(new_triangle_row) - 1):
            new_triangle_row[j_index] = pascal_triangle[rowCount - 1][j_index - 1] + pascal_triangle[rowCount - 1][j_index]
        pascal_triangle.append(new_triangle_row)
        rowCount += 1

    return pascal_triangle[rowIndex]