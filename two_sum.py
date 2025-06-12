def main():
    """
    Calls two_sum_finder on a few sample inputs.
    You can add more test cases here to check your work!
    """
    print(two_sum([2, 7, 11, 15], 9))     # Expected: True
    print(two_sum([1, 2, 3, 4], 8))       # Expected: False
    print(two_sum([5, 5], 10))            # Expected: True
    print(two_sum([4], 8))                # Expected: False

def two_sum(nums, target): # noqa: E501
    """
    Returns True if any two distinct elements in the list `nums`
    add up to the value `target`. Otherwise, returns False.

    Examples:
    two_sum([2, 7, 11, 15], 9) -> True
    two_sum([1, 2, 3, 4], 8) -> False
    """

    for i in range(0, len(nums)): # this loop iterates through the list, checking each number
        num1 = nums[i]
        # first loop gets us the first number to add with
        for j in range(i + 1, len(nums)):
            num2 = nums[j]
            if num1 + num2 == target:
                return True
            # check all the other numbers and if the target sum
            # can be added up

    return False

if __name__ == '__main__':
    main()
