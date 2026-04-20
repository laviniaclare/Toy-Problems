from typing import List

def count_occurences(target:int, nums:List[int]) -> int:
    """
    Takes in a a target and a sorted list of numbers and returns the number of times the target appears.
    We can assume that the input always contains at least one instence of the target.

    Example:
    target -> 7
    nums -> [1,2,3,7,7,7,9,9]
    output -> 3

    Avoid the naive approach of just iterating through the entire list and counting each occurence.
    """
    set_nums = set(nums)
    if len(set_nums) == 1 and target in set_nums:
        return len(nums)

    first_occurence = find_first_occurence(target, nums)
    last_occurence = find_last_occurence(target, nums)

    return last_occurence - first_occurence + 1

def find_first_occurence(target, nums):
    midpoint = len(nums)//2

    curr_index = midpoint
    target_seen = False
    while True:
        if nums[curr_index] > target:
            curr_index -= 1
        elif nums[curr_index] < target:
            if target_seen:
                return curr_index + 1
            curr_index += 1
        else:
            target_seen = True
            curr_index -= 1

def find_last_occurence(target, nums):
    midpoint = len(nums)//2

    curr_index = midpoint
    target_seen = False
    while True:
        if nums[curr_index] > target:
            curr_index -= 1
            if target_seen:
                return curr_index
        elif nums[curr_index] < target:
            curr_index += 1
        else:
            target_seen = True
            curr_index += 1


if __name__ == '__main__':
    print(f'target = {1} and nums = {[1,1,1,1]}')
    print("Output is: ", count_occurences(1, [1,1,1,1]))

    print(f'target = {7} and nums = {[1,2,3,7,7,7,9,9]}')
    print("Output is: ", count_occurences(7, [1,2,3,7,7,7,9,9]))