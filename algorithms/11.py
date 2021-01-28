class BloomFilter:
    def __init__(self, f_len):
        # создаём битовый массив длиной f_len ...
        self.filter_len = f_len
        self.arr = [False] * f_len

    def hash1(self, str1):
        # 17
        res = 0
        for c in str1:
            code = ord(c)
            res = (res * 17) + code
            res = res % self.filter_len
        return res

    def hash2(self, str1):
        # 223
        res = 0
        for c in str1:
            code = ord(c)
            res = (res * 223) + code
            res = res % self.filter_len
        return res

    def add(self, str1):
        # добавляем строку str1 в фильтр
        index1 = self.hash1(str1)
        index2 = self.hash2(str1)

        self.arr[index1] = True
        self.arr[index2] = True

    def is_value(self, str1):
        # проверка, имеется ли строка str1 в фильтре
        index1 = self.hash1(str1)
        index2 = self.hash2(str1)

        if index1 & index2:
            return True
        return False
