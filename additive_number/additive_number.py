class Solution:
    # Not the best solution since I had to use the results array to keep track of the results array 
    # just to assess if the number is additive or not. In addition, I was forced to use alot of conditionals just to contend with 
    # the mulitple edge cases. Will need to optize this solution at a later date.
    def isAdditiveNumber(self, num: str) -> bool:
        # okay so for this problem there are two ways that I can look into solving this.
        # 1.) I can look into this as a sliding window problem but in that vain I will need to contend with backtracking from paths that aren't additive.
        # 2.) The second option is to use backtracking. this will allow me to explore all possible combinations with the caveat of needing to find a backtrack conditional and thinking of a way to record a path that is additive to the next element and paths that are not additive to the next element.

        # easiest first step is to create a results array which will keep track of the states that are additive.

        # create a last conditional that will check if results is empty or not. If so return False else return True

        results = []

        if len(num) >= 3:

            self.recursive_helper(
                [],
                0,
                num,
                results
            )

        return True if len(results) else False

    def recursive_helper(
        self,
        state: List[int],
        index: int,
        num: str,
        results: List[List[int]],
    ):
        # create a conditional that will be the stopping condition (in this case if num is an empty string)
        if len(num) == index and len(state) >= 3 and state[-3] + state[-2] == state[-1]:
            results.append(state[:])
            return 

        for i in range(index, len(num)):
            if len(state) < 2:
                if len(num[index:i+1]) == 1 or num[index:i+1].startswith("0") == False:
                    state.append(int(num[index:i+1]))
                    self.recursive_helper(
                        state,
                        i+1,
                        num,
                        results
                    )
                    state.pop()
            else:
                if len(num[index:i+1]) == 1 or num[index:i+1].startswith("0") == False:
                    if state[-1] + state[-2] == int(num[index:i+1]):
                        state.append(int(num[index:i+1]))
                        self.recursive_helper(
                            state,
                            i+1,
                            num,
                            results
                        )
                        state.pop()