function generate(numRows: number): number[][] {
    const triangle: Array<Array<number>> = [[1], [1,1]]

    if (numRows === 1) {
        return [triangle[0]] 
    }

    let rowCount = 2
    while (numRows > rowCount) {
        rowCount += 1
        let pastRowIndex: number = rowCount - 2
        let rowArray: number[] = new Array(rowCount).fill(1)
        let columnIndex: number = 1
        for (let i: number = 0; i < triangle[pastRowIndex].length - 1; i++) {
            let triangleSum = triangle[pastRowIndex][i] + triangle[pastRowIndex][i+1]
            rowArray[columnIndex] = triangleSum
            columnIndex += 1
        }
        triangle.push(rowArray)
    }

    return triangle
};