from employee import Employee
import unittest

class EmployeeCaseTest(unittest.TestCase):
    def setUp(self):
        self.emp = Employee('wu', 'wei', 150000)

    def test_give_default_raise(self):
        self.emp.give_raise()
        self.assertEqual(self.emp.salary, 155000)

    def test_give_custom_raise(self):
        self.emp.give_raise(10000)
        self.assertEqual(self.emp.salary, 150000)

unittest.main
