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
    # [1,2,3,7,9,9]
    left_index = 0
    right_index = len(nums) - 1
    target_index = None

    while right_index >= left_index:
        curr_index = (right_index + left_index)//2
        if nums[curr_index] > target:
            right_index = curr_index - 1
        elif nums[curr_index] < target:
            left_index = curr_index + 1
        else:
            target_index = curr_index
            right_index = curr_index - 1
    return target_index

            

def find_last_occurence(target, nums):
    left_index = 0
    right_index = len(nums) - 1
    target_index = None

    while right_index >= left_index:
        curr_index = (right_index + left_index)//2
        if nums[curr_index] > target:
            right_index = curr_index - 1
        elif nums[curr_index] < target:
            left_index = curr_index + 1
        else:
            target_index = curr_index
            left_index = curr_index + 1
    return target_index


if __name__ == '__main__':
    print(f'target = {1} and nums = {[1,1,1,1]}')
    print("Output is: ", count_occurences(1, [1,1,1,1]))

    print(f'target = {7} and nums = {[1,2,3,7,7,7,9,9]}')
    print("Output is: ", count_occurences(7, [1,2,3,7,7,7,9,9]))

    print(f'target = {7} and nums = {[1,2,3,7,9,9]}')
    print("Output is: ", count_occurences(7, [1,2,3,7,9,9]))