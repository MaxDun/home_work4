# Определите класс итератор ReverseIter, который принимает список и итерируется по нему в обратном направлении

class ReverseIter:
    def __init__(self, spisok):
        if isinstance(spisok, list):
            self.spisok = spisok
        else:
            raise ValueError('Vvedite spisok')

    def reverse(self):
        self.spisok = self.spisok[::-1]
        for i in self.spisok:
            yield i

a = ReverseIter([1, 2, 3, 'asd'])
for i in a.reverse():
    print(i)
