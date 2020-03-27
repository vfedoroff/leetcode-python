def quicksort(arr=[]):
    if len(arr) == 0:
        return []
    left = []
    right = []
    pivot = arr[0]
    for i in range(1, len(arr), 1):
        if arr[i] < pivot:
            left.append(arr[i])
            continue
        right.append(arr[i])
    return quicksort(left) + [pivot] + quicksort(right)

if __name__ == "__main__":
    result = quicksort([12,4,5,6,7,3,1,15])
    print(result)