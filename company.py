class Employee:

    raise_amount = 1.5

    def __init__(self, first, last, pay, years_in_company):
        self.first = first
        self.last = last
        self.pay = pay
        self.years_in_company = years_in_company

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return f"{self.last}{self.first[0].upper()}@company.uk"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

    def can_be_promoted(self):
        if self.years_in_company > 2:
            return True
        else:
            return False
