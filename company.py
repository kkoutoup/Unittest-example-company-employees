class CompanyDatabaseError(Exception):
    pass

class Employee:

    '''
    Class that creates employee instances based on personal details (first, last name etc).
    Includes method for outputing employee's email address, apply pay rise and promotion.
    '''

    raise_amount = 1.5

    def __init__(self, first, last, pay, years_in_company, can_manage = False):
        self.first = first
        self.last = last
        self.pay = pay
        self.years_in_company = years_in_company
        self.can_manage = can_manage

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

    def add_managees(self):
        if self.can_manage:
            managee_first_name = input("What is the name of the person you're managing? ")
            managee_last_name = input("What is the surname of the person you're managing? ")
            self.employees_managed = []
            self.employees_managed.append([f"{managee_first_name} {managee_last_name}"])
        else:
            raise CompanyDatabaseError("Can't add managees")
            
