from typing import List

def min_dots(segments: List[List[int]]):
    dots = []
    # сортируем отрезки по их концам
    segments.sort(key=lambda seg: seg[1])
    # последняя выбранная точка
    prev_end = -float('inf')
    for seg in segments:
        # начало текущего больше предыдущего конца
        if seg[0] > prev_end:
            # нужно выбирать следующую точку
            # самая лучшая точка - это конец текущего отрезка
            dots.append(seg[1])
            # меняем последнюю выбранную точку
            prev_end = seg[1]

    return dots

print(min_dots([[1, 3], [2, 5], [3, 6]])) # [3]
print(min_dots([[4, 7], [1, 3], [2, 5], [5, 6]])) # [3, 6]
