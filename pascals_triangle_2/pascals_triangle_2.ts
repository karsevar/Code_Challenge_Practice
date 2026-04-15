function getRow(rowIndex: number): number[] {
    let triangle: number[][] = [[1], [1,1]]
    if (rowIndex === 0) {
        return triangle[0]
    }

    if (rowIndex === 1) {
        return triangle[1]
    }

    let rowCount: number = 2
    while (rowCount < rowIndex + 1) {
        rowCount += 1 
        let rowArray: number[] = new Array(rowCount).fill(1);
        let pastRowIndex: number = rowCount - 2
        let columnIndex: number = 1
        for (let i: number = 0; i < triangle[pastRowIndex].length - 1; i++) {
            let columnSum: number = triangle[pastRowIndex][i] + triangle[pastRowIndex][i+1]
            rowArray[columnIndex] = columnSum
            columnIndex += 1
        }
        triangle.push(rowArray)
    }

    return triangle[rowCount - 1]
};