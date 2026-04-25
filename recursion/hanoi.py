def hanoi(n, from_pole, to_pole, aux_pole):
    if n == 1:
        print(f"{from_pole} -> {to_pole}")
        return
    # переносим n - 1 дисков из начальной на вспомогательную
    hanoi(n - 1, from_pole, aux_pole, to_pole)
    print(f"{from_pole} -> {to_pole}")
    # переносим n - 1 дисков из вспомогательной на конечную
    hanoi(n - 1, aux_pole, to_pole, from_pole)

hanoi(2, "1", "3", "2")
print()
hanoi(3, "1", "3", "2")