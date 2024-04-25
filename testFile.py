from Apartment import Apartment
from lab06 import merge_sort, ensure_sorted_ascending, get_best_apartment, get_worst_apartment, get_affordable_apartments

class Test_Apartment:

    def test_init(self):
        a1 = Apartment(600, 1200, 'bad')
        assert a1.get_rent() == 600
        assert a1.get_meters_from_UCSB() == 1200
        assert a1.get_condition() == 'bad'
        assert a1.get_apartment_details() == '(Apartment) Rent: $600, Distance From UCSB: 1200m, Condition: bad'

    def test_get_rent(self):
        a1 = Apartment(600, 1200, 'bad')
        assert a1.get_rent() == 600

    def test_get_meters_from_UCSB(self):
        a1 = Apartment(600, 1200, 'bad')
        assert a1.get_meters_from_UCSB() == 1200

    def test_get_condition(self):
        a1 = Apartment(600, 1200, 'bad')
        assert a1.get_condition() == 'bad'

    def test_get_apartment_details(self):
        a1 = Apartment(600, 1200, 'bad')
        assert a1.get_apartment_details() == '(Apartment) Rent: $600, Distance From UCSB: 1200m, Condition: bad'

    def test_lt(self):
        a1 = Apartment(600, 1200, 'bad')
        a2 = Apartment(600, 1200, 'excellent')
        assert a2 < a1
        a1 = Apartment(600, 1200, 'bad')
        a2 = Apartment(600, 800, 'bad')
        assert a2 < a1
        a1 = Apartment(600, 1200, 'bad')
        a2 = Apartment(500, 1200, 'bad')
        assert a2 < a1

    def test_gt(self):
        a1 = Apartment(600, 1200, 'bad')
        a2 = Apartment(800, 1200, 'bad')
        assert a2 > a1
        a1 = Apartment(600, 1200, 'bad')
        a2 = Apartment(600, 1200, 'excellent')
        assert a1 > a2
        a1 = Apartment(600, 1200, 'bad')
        a2 = Apartment(600, 1000, 'bad')
        assert a1 > a2


    def test_eq(self):
        a1 = Apartment(800, 900, 'average')
        a2 = Apartment(800, 900, 'average')
        assert a1 == a2
        a1 = Apartment(700, 900, 'average')
        a2 = Apartment(800, 900, 'average')
        assert not(a1 == a2)
        a1 = Apartment(700, 900, 'bad')
        a2 = Apartment(700, 900, 'average')
        assert not(a1 == a2)
        a1 = Apartment(700, 900, 'average')
        a2 = Apartment(700, 1000, 'average')
        assert not(a1 == a2)

class Test_lab06:

    def test_merge_sort(self):
        a1 = Apartment(500, 700, 'bad')
        a2 = Apartment(650, 700, 'average')
        a3 = Apartment(1000, 500, 'excellent')
        a4 = Apartment(950, 1000, 'bad')
        alist = [a1, a2, a3, a4]
        merge_sort(alist)
        assert alist == [a1, a2, a4, a3]

        a5 = Apartment(950, 700, 'average')
        a6 = Apartment(950, 500, 'excellent')
        a7 = Apartment(950, 600, 'bad')
        a8 = Apartment(950, 1000, 'bad')
        alist = [a5, a6, a7, a8]
        merge_sort(alist)
        assert alist == [a6, a7, a5, a8]

    def test_ensure_sorted_ascending(self):
        a1 = Apartment(500, 700, 'bad')
        a2 = Apartment(650, 700, 'average')
        a3 = Apartment(1000, 500, 'excellent')
        a4 = Apartment(950, 1000, 'bad')
        alist = [a1, a2, a3, a4]
        assert ensure_sorted_ascending(alist) == False
        merge_sort(alist)
        ensure_sorted_ascending(alist) == True

    def test_get_best_apartment(self):
        a1 = Apartment(500, 700, 'bad')
        a2 = Apartment(650, 700, 'average')
        a3 = Apartment(1000, 500, 'excellent')
        a4 = Apartment(950, 1000, 'bad')
        alist = [a1, a2, a3, a4]
        assert get_best_apartment(alist) == a1.get_apartment_details()

    def test_get_worst_apartment(self):
        a1 = Apartment(650, 700, 'bad')
        a2 = Apartment(650, 700, 'average')
        a3 = Apartment(1000, 500, 'excellent')
        a4 = Apartment(950, 1000, 'bad')
        alist = [a1, a2, a3, a4]
        assert get_worst_apartment(alist) == a3.get_apartment_details()

    def test_get_affordable_apartments(self):
        a1 = Apartment(600, 700, 'bad')
        a2 = Apartment(650, 700, 'average')
        a3 = Apartment(1000, 500, 'excellent')
        a4 = Apartment(950, 1000, 'bad')
        alist = [a1, a2, a3, a4]
        assert get_affordable_apartments(alist, 700) == '(Apartment) Rent: $600, Distance From UCSB: 700m, Condition: bad\n(Apartment) Rent: $650, Distance From UCSB: 700m, Condition: average'
