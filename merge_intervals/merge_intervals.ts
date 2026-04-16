// Best try bruteforce method.
function merge(intervals: number[][]): number[][] {
    // first we will most likely have to sort the array according to the first index of each interval subarray.

    intervals.sort((a,b) => a[0] - b[0])
    console.log("intervals: ", intervals)

    // bruteforce method you can simply iterate over the array checking the second index in the interval index 1 with the first index of the neighboring interval if it's equal to or less then continue to the next interval and do the same step but if not we will combine lowest interval with the highest interval in the series 
    // example [1, 3], [2, 6] becomes [1, 6] because intervals[0][1] 3 is more than intervals[1][0] 2 and we can't move onto interval[2] [8, 10] since 8 is greater than 6. 

    // will need to think about how this can be implemented in code. 

    // we can have a while loop that will terminate if a pointer reaches the end of the array intervals. In addition we can have two pointers left and right. 
    // the left pointer will only move if the interval ends 
    // the right pointer will move to check for matching intervals and if an interval matches the right pointer will continue to iterate until the interval ends.
        // in which case the left pointer will get the index postion of the right pointer and the right pointer will be moved by one. 

    // create a new intervals array that will carry the new intervals values.

    // create a left and right pointer 
    // left pointer will start at the beginning index
    // right pointer will start at the initial + 1 index

    // check if the intervals array is less than 2 
        // if yes return intervals array
    // create a while loop that will terminate once right pointer reaches end of the array will need to have an extra check for if left pointer reaches the end of the array as well.
        // check if intervals[left_pointer][1] >= intervals[right_pointer][0]
        // if no add intervals[left_pointer] to new intervals array and iterate left and right pointers by one
        // if yes:
            // create beginning interval value with intervals[left_pointer][0] this will be the new start point of the resulting interval combination.
            // create a while loop that will terminate when right pointer hits the end of the array or interval[right_pointer][1] < interval[right_pointer + 1][0]
                // iterate right_pointer by one
            // add [intervals[left_pointer][0], intervals[right_pointer][1]] to new intervals array
        // return new intervals array

    const resIntervals: Array<Array<number>> = [];

    if (intervals.length < 2) {
        return intervals
    }

    let rightPointer: number = 1
    let leftPointer: number = 0

    while (leftPointer < intervals.length) {
        // console.log("leftPointer: ", leftPointer, "leftPointer value: ", intervals[leftPointer])
        // console.log("rightPointer: ", rightPointer, "rightPointer value: ", intervals[rightPointer])
        if (leftPointer === intervals.length - 1) {
            resIntervals.push(intervals[leftPointer])
            break
        }
        if (intervals[leftPointer][1] >= intervals[rightPointer][0]) {
            let highestInterval: number = Math.max(intervals[leftPointer][1], intervals[rightPointer][1])
            while (rightPointer + 1 < intervals.length && intervals[rightPointer][1] >= intervals[rightPointer + 1][0]) {
                rightPointer += 1
                if (rightPointer + 1 >= intervals.length) {
                    highestInterval = Math.max(highestInterval, intervals[rightPointer][1])
                } else {
                    highestInterval = Math.max(highestInterval, intervals[rightPointer][1], intervals[rightPointer + 1][1])
                }
            }
            resIntervals.push([intervals[leftPointer][0], highestInterval])
            leftPointer = rightPointer
            rightPointer += 1
            // console.log('leftpointer: ', intervals[leftPointer], "rightPointer: ", intervals[rightPointer])
            leftPointer += 1
            rightPointer += 1

        } else {
            resIntervals.push(intervals[leftPointer])
            leftPointer += 1
            rightPointer += 1
        }
    }



    return resIntervals
};