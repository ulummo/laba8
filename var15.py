class MirrorArray:


    def __init__(self):
        self.data = []

    def read(self):

        n = int(input("Введите количество чисел N: "))
        for i in range(n):
            s = input("Введите число #%d: " % (i + 1)).replace(",", ".")
            self.data.append(float(s))

    def show(self):

        print("Массив:", self.data)

    def count_pairs(self):

        count = 0
        n = len(self.data)
        for j in range(n // 2):
            a = self.data[j]
            b = self.data[n - 1 - j]
            if (a > 0 and b > 0) or (a < 0 and b < 0):
                count += 1
        return count

arr = MirrorArray()
arr.read()
arr.show()
print("Количество зеркальных пар с одинаковым знаком:", arr.count_pairs())
