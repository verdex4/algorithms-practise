def all_subsets(arr, idx=0, subset=[]):
    if idx == len(arr):
        return [subset]

    # все подмножества - это подможества без текущего элемента + подмножества с текущим
    return all_subsets(arr, idx + 1, subset) + all_subsets(arr, idx + 1, subset + [arr[idx]])

subs = all_subsets([1, 2, 3])
for s in subs:
    print(s)