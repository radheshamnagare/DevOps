import unittest
from datetime import date
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options


class TestFramework(unittest.TestCase):	    #inheriting from unittest.TestCase for testing
	
	
	today = date.today()

	# Run before all test cases
	def setUp(self) -> None:			#class methods
		return super().setUp()

	# Run after all test cases are done
	def tearDown(self) -> None:
		return super().tearDown()

	def test_date(self):
		self.assertTrue(self.today)

	'''def test(self):
		try:
			tb.get_Data(self.username,self.password,self.baseURL)
			chrome_options = Options()
			chrome_options.add_experimental_option("detach", True)
			self.driver=webdriver.Chrome()
			self.driver.get(self.baseURL)
			html=self.driver.page_source
			soup=BeautifulSoup(html,"html.parser")


		except TimeoutException as e:
			print(e)
			print("Timeout")
			self.driver.close()'''


	# Returns True if the string contains 4 a.
	def test_strings_a(self):
		self.assertEqual( 'a'*4, 'aaaa')

	# Returns True if the string is in upper case.
	def test_upper(self):		
		self.assertEqual('try'.upper(), 'TRY')

	# Returns TRUE if the string is in uppercase
	# else returns False.
	def test_isupper(self):		
		self.assertTrue('TRY'.isupper())
		self.assertFalse('Try'.isupper())

	# Returns true if the string is stripped and
	# matches the given output.
	def test_strip(self):		
		s = 'finmarkatesting'							#remove 'f,i,n,m,a,r,k' letters
		self.assertEqual(s.strip('finmark'), 'atesting') #finmarkatesting-finmark=testing !=testing

	# Returns true if the string splits and matches
	# the given output.
	def test_split(self):		
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 2])
		with self.assertRaises(TypeError):              #exception handeling 
			s.split(2)

	def test_list_int(self):
		data = [1, 2, 3, 4, 5]
		result = sum(data)
		self.assertEqual(result, 15)

	def test_add(self):
		addition=10+2
		self.assertEqual(addition,30)


if __name__ == '__main__':
	unittest.main()


#all the functions(def test_...) are built-in functions of unittest module

#all the method names must start with "test_" because of unnittest module naming convension

#unnittest.main() provides a command-line interface to run the test script

