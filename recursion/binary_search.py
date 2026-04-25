def recursive_binary_search(arr, target, l=None, r=None):
    if l is None and r is None:
        l = 0 # указатель на начальный элемент
        r = len(arr) - 1 # указатель на последний элемент
    if l > r:
        return -1
    
    mid = l + (r - l) // 2
    if arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, r)
    elif arr[mid] > target:
        return recursive_binary_search(arr, target, l, mid - 1)
    else:
        return mid

print(recursive_binary_search([1, 3, 5, 7, 9, 11], target=7)) # 3
print(recursive_binary_search([1, 5, 6, 7, 9, 10, 13, 16, 18], target=5)) # 1
print(recursive_binary_search([1, 2, 3, 4, 5, 6, 7, 9, 10], target=8)) # -1