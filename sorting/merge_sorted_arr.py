def merge_sorted_arr(a, b):
    result = []
    pos1, pos2 = 0, 0

    while pos1 < len(a) or pos2 < len(b):
        if pos1 == len(a):
            result.append(b[pos2])
            pos2 += 1
        elif pos2 == len(b):
            result.append(a[pos1])
            pos1 += 1
        elif a[pos1] <= b[pos2]:
            result.append(a[pos1])
            pos1 += 1
        else:
            result.append(b[pos2])
            pos2 += 1
    
    return result

if __name__ == "__main__":
    print(merge_sorted_arr([1, 2, 7], [1, 3, 5])) # [1, 1, 2, 3, 5, 7]
    print(merge_sorted_arr([1, 2, 3, 6, 7], [2, 6, 8, 10, 12, 15])) # [1, 2, 2, 3, 6, 6, 7, 8, 10, 12, 15]