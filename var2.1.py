def main():
    m = int(input("Введите порядок массива (нечётное число): "))

    if m % 2 == 0:
        print("Ошибка: порядок должен быть нечётным.")
        return

    print("Введите", m, "строк по", m, "чисел:")
    a = []
    for i in range(m):
        row = [float(x.replace(",", ".")) for x in input().split()]
        a.append(row)

    c = m // 2
    center = abs(a[c][c])

    print("Результат:")
    for r in range(c + 1):
        count = 0

        for i in range(c - r, c + r + 1):
            for j in range(c - r, c + r + 1):
                if abs(a[i][j]) > center:
                    count += 1

        print("Порядок %d: %d" % (2 * r + 1, count))


if __name__ == "__main__":
    main()
