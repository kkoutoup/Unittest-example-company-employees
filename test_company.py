import unittest
from company import Employee, Manager, CompanyDatabaseError

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

# Test Manager subclass
class TestManagerCreation(unittest.TestCase):

  '''
  Create re-usable cases for tests that follow
  '''
  def setUp(self):
    self.manager_1 = Manager("John", "Smith", 50000, 3)
    self.manager_2 = Manager("Kristen", "Stewart", 60000, 5, "Judy")

  def test_manager_employees(self):
    '''
    Test that employees are added upon instance creation
    '''
    self.assertEqual(self.manager_2.employees, ["Judy"])

  def test_manager_add_employee_that_already_exists(self):
    '''
    Should raise exception if employee has already been added
    '''
    self.manager_1.add_employee("Kostas")
    with self.assertRaises(CompanyDatabaseError):
      self.manager_1.add_employee("Kostas")

  def test_manager_add_employee(self):
    '''
    Testing method works
    '''
    self.manager_1.add_employee("Kostas")
    self.manager_1.add_employee("John")
    self.assertEqual(self.manager_1.employees, ["Kostas", "John"])

  def test_manager_remove_employee_when_no_employees(self):
    '''
    Raise exception if employees list is empty
    '''
    with self.assertRaises(CompanyDatabaseError):
      self.manager_1.remove_employee("Kostas")

  def test_manager_remove_employee_when_employee_not_there(self):
    '''
    Raise exception if employee hasn't been added
    '''
    self.manager_1.add_employee("Jimi")
    with self.assertRaises(CompanyDatabaseError):
      self.manager_1.remove_employee("Johnny")

  def test_manager_remove_employee(self):
    '''
    Testing method works
    '''
    self.manager_2.remove_employee("Judy")
    self.assertEqual(self.manager_2.employees, [])

  def test_manager_list_employees_when_list_is_empty(self):
    '''
    Raise exception if employees array is empty
    '''
    with self.assertRaises(CompanyDatabaseError):
      self.manager_1.list_employees()

  def test_manager_fullname(self):
    '''
    Testing inherited fullname method works
    '''
    self.assertEqual(self.manager_1.fullname, "John Smith")
    self.assertEqual(self.manager_2.fullname, "Kristen Stewart")

  def test_manager_email(self):
    '''
    Testing inherited email method works
    '''
    self.assertEqual(self.manager_1.email, "SmithJ@company.uk")
    self.assertEqual(self.manager_2.email, "StewartK@company.uk")

  def test_manager_apply_raise(self):
    '''
    Testing inherited apply_raise method works
    '''
    raise_manager_1 = self.manager_1.apply_raise()
    self.assertEqual(raise_manager_1, 90000)

    raise_manager_2 = self.manager_2.apply_raise()
    self.assertEqual(raise_manager_2, 108000)

if __name__ == '__main__':
    unittest.main()

    
