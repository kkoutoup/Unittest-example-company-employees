import unittest
from company import Employee, CompanyDatabaseError

# Test Employee class
class TestEmployeeCreation(unittest.TestCase):
    
  def setUp(self):
    '''
    Creates re-usable cases for tests that follow
    '''
    self.emp_1 = Employee("Kostas", "Koutoupis", 30000, 3)
    self.emp_2 = Employee("Sue", "Weatherspoon", 20000, 2)   
        
  def test_employee_fullname(self):
    '''
    Fullname method should combine employee's first and last name
    '''
    emp_1_fullname = self.emp_1.fullname
    self.assertEqual(emp_1_fullname, "Kostas Koutoupis")
    
    emp_2_fullname = self.emp_2.fullname
    self.assertEqual(self.emp_2.fullname, "Sue Weatherspoon")
      
  def test_employee_email(self):
    '''
    Email method should combine lastname and uppercase of
    first name's first letter with @company.uk
    '''
    email1 = self.emp_1.email
    self.assertEqual(email1, "KoutoupisK@company.uk")

    email2 = self.emp_2.email
    self.assertEqual(email2, "WeatherspoonS@company.uk")

  def test_employee_email_regex(self):
    '''
    Testing email structure against regex
    '''
    email1 = self.emp_1.email
    self.assertRegex(email1, r"[\w]+[\w]@company\.uk")

    email2 = self.emp_2.email
    self.assertRegex(email2, r"[\w]+[\w]@company\.uk")

  def test_employee_apply_raise(self):
    '''
    Apply raise should multiply pay with raise amount
    '''
    raise_emp_1 = self.emp_1.apply_raise()
    self.assertEqual(raise_emp_1, 45000)

    raise_emp_2 = self.emp_2.apply_raise()
    self.assertEqual(raise_emp_2, 30000)

  def test_employee_can_be_promoted(self):
    '''
    If employee years in the company > 2
    then this should return True
    '''
    promotion_1 = self.emp_1.can_be_promoted()
    self.assertTrue(promotion_1)

    promotion_2 = self.emp_2.can_be_promoted()
    self.assertFalse(promotion_2)

if __name__ == "__main__":
  unittest.main()