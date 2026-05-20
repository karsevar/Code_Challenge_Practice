class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # it seems that this is another sequence sub array problem.
        # the main standout is that we are only allowed two separate fruit baskets which means that we are only allowed to collect two different types of fruit. So perhaps I can change this into some kind of a hashmap problem where I keep track of the fruit count and times in some kind of a hashmap. The issue with this is that the sequence will need to be maintained. I think I can just simply use a set to store the fruit types that I run into and if the set exceeds two than I iterate index i 

        # create a maximum fruit count
        
        # create a for loop that will keep track of index i
        # create a set that will keep track of the fruit types
        # add fruits[i] type to set
        # create current frequency counter

        # create a for loop that will keep track of index j
        # check if fruit type is in set

        # time complexity is O(n^2) since we are looping through the array twice in a nested for loop


        maximum_count = 0

        if len(fruits) <= 1:
            maximum_count = len(fruits)

        for i in range(len(fruits) - 1):
            current_count = 1
            fruit_type_set = set()
            fruit_type_set.add(fruits[i])
            for j in range(i + 1, len(fruits)):
                if fruits[j] in fruit_type_set:
                    current_count += 1
                else:
                    if len(fruit_type_set) == 1:
                        fruit_type_set.add(fruits[j])
                        current_count += 1
                    else:
                        if maximum_count < current_count:
                            maximum_count = current_count
                        break

            if maximum_count < current_count:
                maximum_count = current_count

        return maximum_count