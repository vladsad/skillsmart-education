import unittest


# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
class PowerSet:

    def __init__(self):
        # ваша реализация хранилища
        self.pset = []
        self._step = 1

    def size(self):
        # количество элементов в множестве
        return len(self.pset)

    def hash_fun(self, value):
        index = len(str(value).encode('utf-8')) % self.size()
        return index

    def seek_slot(self, value):
        # находит индекс пустого или уже созданного слота для значения, или None
        counter = 0
        index = self.hash_fun(value)
        if self.pset[index] is None:
            return index
        while counter < self.size():
            index = index + self._step
            if index >= self.size():
                index = index - self.size()
            if self.pset[index] is None:
                return index
            if self.pset[index] is value:
                return index
            counter = counter + 1
        return None

    def put(self, value):
        # всегда срабатывает
        if self.size() == 0:
            self.pset.append(value)
        else:
            index = self.seek_slot(value)
            if index is None:
                self.pset.append(value)
            else:
                self.pset[index] = value
        return None

    def get(self, value):
        # возвращает True если value имеется в множестве,
        # иначе False
        if value in self.pset:
            return True
        return False

    def remove(self, value):
        # возвращает True если value удалено
        # иначе False
        try:
            index = self.pset.index(value)
            del self.pset[index]
            return True
        except ValueError:
            return False

    def intersection(self, set2):
        # пересечение текущего множества и set2
        new_pset = PowerSet()

        len_1 = self.size()
        len_2 = set2.size()
        min_len = len_2 if len_1 > len_2 else len_1

        for i in range(min_len):
            if self.pset[i] in set2.pset:
                new_pset.put(self.pset[i])
            if set2.pset[i] in self.pset:
                new_pset.put(set2.pset[i])

        if len_1 > len_2:
            for i in range(min_len, len_1):
                if self.pset[i] in set2.pset:
                    new_pset.put(self.pset[i])
        else:
            for i in range(min_len, len_2):
                if set2.pset[i] in self.pset:
                    new_pset.put(set2.pset[i])

        return new_pset

    def union(self, set2):
        # объединение текущего множества и set2
        new_pset = PowerSet()
        new_pset.pset = self.pset[::]
        for i in set2.pset:
            new_pset.put(i)
        return new_pset

    def difference(self, set2):
        # разница текущего множества и set2
        new_pset = PowerSet()
        for i in self.pset:
            if set2.get(i) is False:
                new_pset.put(i)
        return new_pset

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        for i in set2.pset:
            if self.get(i) is True:
                pass
            else:
                return False
        return True


class TestUM(unittest.TestCase):
    def setUp(self):
        self.set1 = PowerSet()
        self.set2 = PowerSet()

    def test_put(self):
        self.set1.put(1)
        self.assertEqual(1, self.set1.pset[0])
        self.assertEqual(1, self.set1.size())

        self.set1.put('1')
        self.assertEqual('1', self.set1.pset[1])
        self.assertEqual(2, self.set1.size())

        self.set1.put('vlad')
        self.assertEqual('vlad', self.set1.pset[2])
        self.assertEqual(3, self.set1.size())

        self.set1.put(1)
        self.assertEqual(3, self.set1.size())
        self.set1.put('1')
        self.assertEqual(3, self.set1.size())
        self.set1.put('vlad')
        self.assertEqual(3, self.set1.size())

    def test_remove(self):
        self.set1.put(1)
        self.set1.put('1')
        self.set1.put(0)
        self.set1.put('vlad')

        self.assertEqual(True, self.set1.remove('1'))
        self.assertEqual(3, self.set1.size())
        self.assertEqual(0, self.set1.pset[1])

        self.assertEqual(True, self.set1.remove(1))
        self.assertEqual(2, self.set1.size())
        self.assertEqual(0, self.set1.pset[0])

        self.assertEqual(True, self.set1.remove('vlad'))
        self.assertEqual(1, self.set1.size())
        self.assertEqual(0, self.set1.pset[0])

        self.assertEqual(False, self.set1.remove('0'))
        self.assertEqual(1, self.set1.size())
        self.assertEqual(0, self.set1.pset[0])

    def test_intersection(self):
        self.set1.put(1)
        self.set1.put('1')
        self.set1.put(0)
        self.set1.put('vlad')

        self.set2.put(1)
        self.set2.put('2')
        self.set2.put('test')
        self.set2.put('test2')
        self.set2.put('vlad')

        new_pset1 = self.set1.intersection(self.set2)
        self.assertEqual(2, new_pset1.size())
        self.assertEqual(True, new_pset1.get(1))
        self.assertEqual(True, new_pset1.get('vlad'))

        set3 = PowerSet()
        set4 = PowerSet()

        set3.put(1)
        set3.put('1')
        set3.put(0)
        set3.put('vlad')
        set3.put('test2')

        set4.put(2)
        set4.put('2')
        set4.put(3)
        set4.put('test')

        new_pset2 = set3.intersection(set4)
        self.assertEqual(0, new_pset2.size())
        self.assertEqual(False, new_pset2.get(1))
        self.assertEqual(False, new_pset2.get('vlad'))

    def test_union(self):
        self.set1.put(1)
        self.set1.put('1')
        self.set1.put(0)
        self.set1.put('vlad')

        self.set2.put(1)
        self.set2.put('2')
        self.set2.put('test')
        self.set2.put('test2')
        self.set2.put('vlad')

        new_pset1 = self.set1.union(self.set2)
        self.assertEqual(7, new_pset1.size())
        self.assertEqual(True, new_pset1.get(1))
        self.assertEqual(True, new_pset1.get('test2'))
        self.assertEqual(False, new_pset1.get('test3'))

        set3 = PowerSet()
        set4 = PowerSet()

        set3.put(1)
        set3.put('1')
        set3.put(0)
        set3.put('vlad')
        set3.put('test2')

        new_pset2 = set3.union(set4)
        self.assertEqual(5, new_pset2.size())
        self.assertEqual(True, new_pset2.get(1))
        self.assertEqual(True, new_pset2.get('vlad'))

    def test_difference(self):
        self.set1.put(1)
        self.set1.put('1')
        self.set1.put(0)
        self.set1.put('vlad')

        self.set2.put(1)
        self.set2.put('2')
        self.set2.put('test')
        self.set2.put('test2')
        self.set2.put('vlad')

        new_pset1 = self.set1.difference(self.set2)
        self.assertEqual(2, new_pset1.size())
        self.assertEqual(True, new_pset1.get('1'))
        self.assertEqual(True, new_pset1.get(0))
        self.assertEqual(False, new_pset1.get('vlad'))

        set3 = PowerSet()
        set4 = PowerSet()

        set3.put(1)
        set3.put('1')
        set3.put(0)
        set3.put('vlad')
        set3.put('test2')

        set4.put(2)
        set4.put('2')
        set4.put(3)
        set4.put('test')

        new_pset2 = set3.difference(set4)
        self.assertEqual(5, new_pset2.size())
        self.assertEqual(True, new_pset2.get(1))
        self.assertEqual(True, new_pset2.get('vlad'))
        self.assertEqual(False, new_pset2.get('test'))

        set5 = PowerSet()
        set6 = PowerSet()

        set5.put(1)
        set5.put('1')

        set6.put(2)
        set6.put('2')
        set6.put(3)
        set6.put(1)
        set6.put('test')
        set6.put('1')

        new_pset3 = set5.difference(set6)
        self.assertEqual(0, new_pset3.size())
        self.assertEqual(False, new_pset3.get(1))
        self.assertEqual(False, new_pset3.get('vlad'))
        self.assertEqual(False, new_pset3.get('test'))

    def test_issubset(self):
        self.set1.put(1)
        self.set1.put('1')
        self.set1.put('test')
        self.set1.put('vlad')
        self.set1.put('test2')
        self.set1.put(0)

        self.set2.put(1)
        self.set2.put('1')
        self.set2.put(0)
        self.set2.put('vlad')

        self.assertEqual(True, self.set1.issubset(self.set2))
        self.assertEqual(True, self.set1.get(1))
        self.assertEqual(True, self.set1.get('1'))
        self.assertEqual(True, self.set1.get(0))
        self.assertEqual(True, self.set1.get('vlad'))

        set3 = PowerSet()
        set4 = PowerSet()

        set3.put(1)
        set3.put('1')
        set3.put(0)
        set3.put('vlad')

        set4.put(1)
        set4.put('1')
        set4.put('test')
        set4.put('vlad')
        set4.put('test2')
        set4.put(0)

        self.assertEqual(False, set3.issubset(set4))
        self.assertEqual(True, set3.get(1))
        self.assertEqual(True, set3.get('1'))
        self.assertEqual(True, set3.get(0))
        self.assertEqual(True, set3.get('vlad'))
        self.assertEqual(False, set3.get('test'))
        self.assertEqual(True, set4.get(1))
        self.assertEqual(True, set4.get('1'))
        self.assertEqual(True, set4.get(0))
        self.assertEqual(True, set4.get('vlad'))

        set5 = PowerSet()
        set6 = PowerSet()

        set5.put(1)
        set5.put('1')
        set5.put('test')
        set5.put('vlad')
        set5.put('test2')
        set5.put(0)

        set6.put(1)
        set6.put('3')
        set6.put('vlad')

        self.assertEqual(False, set5.issubset(set6))
        self.assertEqual(True, set5.get(1))
        self.assertEqual(True, set5.get('1'))
        self.assertEqual(True, set5.get(0))
        self.assertEqual(True, set5.get('vlad'))
        self.assertEqual(True, set6.get('vlad'))
        self.assertEqual(False, set5.get('3'))
        self.assertEqual(True, set6.get('3'))


if __name__ == '__main__':
    unittest.main()
