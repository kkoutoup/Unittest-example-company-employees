class CompanyDatabaseError(Exception):
    '''
    Create a custom error inheriting from Exception class
    '''
    pass

class Employee:

    '''
    Class that creates employee instances based on personal details (first, last name etc).
    Includes method for outputing employee's email address, apply pay rise and promotion.
    '''

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


class Manager(Employee):
  '''
  Inherits from Employee class
  '''
  raise_amount = 1.8

  def __init__(self, first, last, pay, years_in_company, employees = None):
    super().__init__(first, last, pay, years_in_company)
    if employees is None:
        self.employees = []
    else:
        self.employees = [employees]

  def add_employee(self, employee_name):
    if employee_name in self.employees:
      raise CompanyDatabaseError("Employee already in the company's database")
    else:
      self.employees.append(employee_name)

  def remove_employee(self, employee_name):
    if self.employees == []:
        raise CompanyDatabaseError("No employees have been added yet")
    else:
        if employee_name in self.employees:
            self.employees.remove(employee_name)
        else:
          raise CompanyDatabaseError("Employee not found in the company's database")

  def list_employees(self):
    if len(self.employees) == 0:
        raise CompanyDatabaseError("No employees have been added so far")
    else:
        for employee in self.employees:
            print(employee)
