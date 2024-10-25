def binary_search(arr, target):
    low, high  = 0, len(arr)-1

    while low <= high:
        mid = low + (high-low)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f" Result found at Index {result}")
else:
    print("Element not found !")
