from merge_sorted_arr import merge_sorted_arr

def merge_sort(arr):
    if len(arr) <= 1:
        # список длины 1 и меньше уже отсортирован
        return arr

    mid = len(arr) // 2
    # объединяем отсортированные левую и правую половины
    return merge_sorted_arr(
        merge_sort(arr[:mid]),
        merge_sort(arr[mid:])
    )

print(merge_sort([3, 1, 2, 4, 5])) # [1, 2, 3, 4, 5]
print(merge_sort([11, 3, 4, 9, 10, 8])) # [3, 4, 8, 9, 10, 11]
