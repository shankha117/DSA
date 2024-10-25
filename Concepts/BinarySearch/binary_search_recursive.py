def binary_search(arr, low, high, target):
    if high >= low:
        mid = low + (high - low) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid

        # If target is smaller, search in the left subarray
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)

        # Otherwise, search in the right subarray
        else:
            return binary_search(arr, mid + 1, high, target)

    # If target is not present
    return -1

# Example usage
arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search(arr, 0, len(arr) - 1, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
