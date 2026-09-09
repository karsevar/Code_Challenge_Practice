class Solution:
    # Bruteforce solution where we are deciding whether to go down or right within a n * m grid. 
    # I believe that the time complexity can be conceptualized as O(2m*n).
    def uniquePaths(self, m: int, n: int) -> int:
        # okay so the stopping condition is m and n going to m and n which will increment the counter of possible paths the robot can take to reach the finish line.
        # the robot can only go right or down.

        # create a recursion function that will take m and n as arguments and m_index and n_index. the index counter parts will be initialized as 1 respectively. 
        # the main question is how I should set up the recursion steps.
        # Perhaps we can do a recursive call that will do the right movement and another call that will do the down movement.
        # base cases will be if m_index is equal to m but n_index less than n return a zero and n_index is equal to n but m_index is less than m return a zero.
        # the final case will be if both m and n are equal to n_index and m_index than return 1 

        return self.recursion_helper(
            1,
            1,
            m,
            n,
        )

    def recursion_helper(self, m_index: int, n_index: int, m: int, n: int) -> int:
        # print("m_index: ", m_index, " n_index: ", n_index)
        if m_index > m and n_index < n:
            return 0
        elif n_index > n and m_index < m:
            return 0
        elif m_index == m and n_index == n:
            return 1

        right_movement = self.recursion_helper(m_index, n_index+1, m, n)
        down_movement = self.recursion_helper(m_index +1, n_index, m, n)

        return right_movement + down_movement

class SolutionCache:
    # Bruteforce with additional cache. I believe that this roughly decreased the time complexity to O(m*n)
    # as we are to reprocessing already calculated n_index and m_index positions.
    # space complexity can be regarded as O(m*n) as we are creating a cache within the recursion function.
    def uniquePaths(self, m: int, n: int) -> int:
        # okay so the stopping condition is m and n going to m and n which will increment the counter of possible paths the robot can take to reach the finish line.
        # the robot can only go right or down.

        # create a recursion function that will take m and n as arguments and m_index and n_index. the index counter parts will be initialized as 1 respectively. 
        # the main question is how I should set up the recursion steps.
        # Perhaps we can do a recursive call that will do the right movement and another call that will do the down movement.
        # base cases will be if m_index is equal to m but n_index less than n return a zero and n_index is equal to n but m_index is less than m return a zero.
        # the final case will be if both m and n are equal to n_index and m_index than return 1 

        return self.recursion_helper(
            1,
            1,
            m,
            n,
            {}
        )

    def recursion_helper(self, m_index: int, n_index: int, m: int, n: int, cache: dict[tuple[int], int]) -> int:
        if m_index > m and n_index < n:
            return 0
        elif n_index > n and m_index < m:
            return 0
        elif m_index == m and n_index == n:
            return 1

        if (m_index, n_index) in cache:
            return cache[(m_index, n_index)]

        right_movement = self.recursion_helper(m_index, n_index+1, m, n, cache)
        down_movement = self.recursion_helper(m_index +1, n_index, m, n, cache)

        cache[(m_index, n_index)] = right_movement + down_movement
        return cache[(m_index, n_index)]