"""test cities"""
import unittest
from city_functions import city_add,Employee

class Teststr(unittest.TestCase):
	def test_city_country(self):
		#这里调用断言方法来判断程序是否有误
		self.assertEqual('santiago,chile', city_add('santiago', 'chile'))
		
	def test_more_city_country(self):
		self.assertEqual('santiago,chile- population5000', city_add('santiago', 'chile',5000))
	
#unittest.main()

#断言方法：
#assertEqual(a,b)  a==b
#assertNotEqual(a,b) a!=b
#assertTrue(x)	x=True
#assertFalse(x) x=False
#assertIn(item,list)  item在list中
#assertNotIn(item,list) item不在list中


#11.3
class InfoTest(unittest.TestCase):
	def setUp(self):
		self.fname = 'ye'
		self.lname = 'feng'
		self.money = 4300
		self.emp = Employee(self.fname, self.lname, self.money )
		
	def test_give_defaultraise(self):
		self.emp.give_raise(1000)
		self.assertEqual(self.fname, self.emp.first_name)
		self.assertEqual(self.lname,  self.emp.last_name)
		self.assertEqual(self.emp.money, 5300)
	
	def test_give_custom_raise(self):
		self.emp.give_raise()
		self.assertEqual(self.fname, self.emp.first_name)
		self.assertEqual(self.lname,  self.emp.last_name)
		self.assertEqual(self.emp.money, 9300)


unittest.main()



















