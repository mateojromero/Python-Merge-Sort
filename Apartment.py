
class Apartment:
    def __init__(self, rent, meters_from_UCSB, condition):
        self.rent = rent
        self.meters_from_UCSB = meters_from_UCSB
        self.condition = condition

    def get_rent(self):
        return self.rent

    def get_meters_from_UCSB(self):
        return self.meters_from_UCSB

    def get_condition(self):
        return self.condition
    
    def get_apartment_details(self):
        return (f'(Apartment) Rent: ${self.rent}, Distance From UCSB: {self.meters_from_UCSB}m, Condition: {self.condition}')

    def condition_order(self):
        order = {'bad': 1, 'average': 2, 'excellent': 3}
        return order[self.condition]

    def __lt__(self, other):
        if self.rent < other.rent:
            return True
        elif self.rent == other.rent:
            if self.meters_from_UCSB < other.meters_from_UCSB:
                return True
            elif self.meters_from_UCSB == other.meters_from_UCSB:
                return self.condition_order() > other.condition_order()
        return False

    def __gt__(self, other):
        if self.rent > other.rent:
            return True
        elif self.rent == other.rent:
            if self.meters_from_UCSB > other.meters_from_UCSB:
                return True
            elif self.meters_from_UCSB == other.meters_from_UCSB:
                return self.condition_order() < other.condition_order()
        return False

    def __eq__(self, other):
        if self.rent == other.rent:
            if self.meters_from_UCSB == other.meters_from_UCSB:
                if self.condition == other.condition:
                    return True
                else:
                    return False
            return False
        return False
