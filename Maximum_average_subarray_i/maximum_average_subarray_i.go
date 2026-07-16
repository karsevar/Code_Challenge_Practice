func findMaxAverage(nums []int, k int) float64 {
    // create a maximum sum variable first
    var current_sum int = Sum(nums[:k]...)
    var maximum_sum int = current_sum
    var tail_index int = 0

    for i := k; i < len(nums); i++ {
        current_sum -= nums[tail_index]
        current_sum += nums[i] 

        tail_index += 1

        if current_sum > maximum_sum {
            maximum_sum = current_sum
        }
    }
    return float64(maximum_sum) / float64(k)
}

func Sum(input ...int) int {
    sum := 0

    for i := range input {
        sum += input[i]
    }

    return sum
}