def binary_search_rotated(arr, target, rotation_index):
    """
    Perform binary search on a rotated sorted array.
    
    :param arr: List[int] - The rotated sorted array.
    :param target: int - The number to search for.
    :param rotation_index: int - The index at which the array was rotated.
    :return: bool - True if the target is in the array, False otherwise.
    """
    if not arr:
        return False
    
    n = len(arr)
    
    # If rotation_index is 0, array is not rotated
    if rotation_index == 0:
        left, right = 0, n - 1
    else:
        # Determine which half the target belongs to
        if target >= arr[0]:  # Target is in the left sorted half
            left, right = 0, rotation_index - 1
        else:  # Target is in the right sorted half
            left, right = rotation_index, n - 1
    
    def binary_search(arr, left, right, target):
        """
        Performs a binary search on a sorted array within the specified range.
        
        :param arr: List[int] - The sorted array to search in.
        :param left: int - The left boundary of the search range (inclusive).
        :param right: int - The right boundary of the search range (inclusive).
        :param target: int - The value to search for.
        :return: bool - True if the target is in the array, False otherwise.
        """
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
    # Perform binary search on the determined half
    return binary_search(arr, left, right, target)

# Example usage:
arr = [4, 5, 6, 7, 0, 1, 2]
target = 0
rotation_index = 4
print(binary_search_rotated(arr, target, rotation_index))  # Output: True
