class Sorter:
    def sort(self, l):
        pass


class Sorter1(Sorter):
    def sort(self, l):
        l.sort()
        return l


class Sorter2(Sorter):
    def sort(self, l):
        return sorted(l)


def sort_list(l, sorter: Sorter):
    print(sorter.sort(l))


s1 = Sorter1()
s2 = Sorter2()

l = [1, 2, 3, 4, 5, 6, 7, 8]

sort_list(l, s2)
sort_list(l, s1)
sort_list(l, 4)
