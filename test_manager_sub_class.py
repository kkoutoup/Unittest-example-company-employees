import unittest
from company import Employee, Manager, CompanyDatabaseError

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

  def test_manager_email_regex(self):
      '''
      Testing inherited method against regex
      '''
      email1 = self.manager_1.email
      self.assertRegex(email1, r"[\w]+[\w]@company\.uk")

      email2 = self.manager_2.email
      self.assertRegex(email2, r"[\w]+[\w]@company\.uk")

  def test_manager_apply_raise(self):
    '''
    Testing inherited apply_raise method works
    '''
    raise_manager_1 = self.manager_1.apply_raise()
    self.assertEqual(raise_manager_1, 90000)

    raise_manager_2 = self.manager_2.apply_raise()
    self.assertEqual(raise_manager_2, 108000)

    
