## Find First and Last Position of Element in Sorted Array
#  https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


def search_range(nums, target):
    """Finds the first and last positions of a target element in a sorted array.

  Args:
    nums: A sorted array of integers.
    target: The target element to search for.

  Returns:
    A list of two integers, where the first element is the first occurrence of the
    target element in the array, and the second element is the last occurrence of the
    target element in the array. If the target element is not found in the array,
    then the list will contain two -1 values.
  """

    ans = [-1, -1]
    # Find the first occurrence of the target element.
    ans[0] = search(nums, target, True)
    if ans[0] != -1:
        # Find the last occurrence of the target element.
        ans[1] = search(nums, target, False)
    return ans


def search(nums, target, find_start_index):
    """Finds the index of a target element in a sorted array.

  Args:
    nums: A sorted array of integers.
    target: The target element to search for.
    find_start_index: A boolean value indicating whether to find the start index
      of the target element (True) or the end index (False).

  Returns:
    The index of the target element in the array, or -1 if the target element
    is not found in the array.
  """

    ans = -1
    start = 0
    end = len(nums) - 1
    while start <= end:
        # Find the middle element.
        mid = (start + end) // 2
        if target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            start = mid + 1
        else:
            # Potential answer found.
            ans = mid
            if find_start_index:
                end = mid - 1
            else:
                start = mid + 1
    return ans


if __name__ == '__main__':
    nums = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
    target = 8
    ans = search_range(nums, target)
    print(ans)
