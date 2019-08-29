"""Android Calculator App Test: DEL Button"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from tests.android_v7.calculator_tests.calculator_base_testcase import AndroidCalculatorBaseTestCase


@allure.epic('Android Native App')
@allure.parent_suite('Functional Test')
@allure.suite("Calculator Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("Clear Screen Functionality")
@allure.story('DEL Button')
class TestDelBtnCase(AndroidCalculatorBaseTestCase):
	"""
	Android Calculator App Test: DEL Button
	
	Should be able to clear the screen after inserting a negative floating point number
	Should be able to clear the screen after inserting an positive floating point number
	Should be able to clear the screen after inserting a negative integer
	Should be able to clear the screen after inserting a positive integer
	Should allow clear to be pressed multiple times
	Should be able to clear after inserting a many digit floating point number
	Should be able to clear after inserting a negative many digit floating point number
	Should be able to clear after inserting a large negative integer
	Should be able to clear after inserting a large integer

	Source: http://mozilla.github.io/calculator/test/?grep=Unit%20Tests%20Division
	"""

	def test_clear_the_screen_after_inserting_a_negative_floating_point_number(self):
		"""
		Should be able to clear the screen after inserting a negative floating point number
		-12.3 C -> 0
		:return:
		"""
		allure.dynamic.title("Clear the screen after inserting a negative floating point number test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Clear the screen after inserting a negative floating point number"):
			self.enter_number(-12.3)
			self.app.del_btn.tap()
			assert self.app.screen_result.label == ''

	def test_clear_the_screen_after_inserting_an_positive_floating_point_number(self):
		"""
		Should be able to clear the screen after inserting an positive floating point number
		12.3 C -> 0
		:return:
		"""
		allure.dynamic.title("Clear the screen after inserting an positive floating point number test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("clear the screen after inserting an positive floating point number"):
			self.enter_number(12.3)
			self.app.del_btn.tap()
			assert self.app.screen_result.label == ''

	def test_clear_the_screen_after_inserting_a_negative_integer(self):
		"""
		Should be able to clear the screen after inserting a negative integer
		-123 C -> 0
		:return:
		"""
		allure.dynamic.title("Clear the screen after inserting a negative integer test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Clear the screen after inserting a negative integer"):
			self.enter_number(-123)
			self.app.del_btn.tap()
			assert self.app.screen_result.label == ''

	def test_clear_the_screen_after_inserting_a_positive_integer(self):
		"""
		Should be able to clear the screen after inserting a positive integer
		123 C -> 0
		:return:
		"""
		allure.dynamic.title("Clear the screen after inserting a positive integer test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Clear the screen after inserting a positive integer"):
			self.enter_number(123)
			self.app.del_btn.tap()
			assert self.app.screen_result.label == ''

	def test_clear_to_be_pressed_multiple_times(self):
		"""
		Should allow clear to be pressed multiple times
		123456789 C C C -> 0
		:return:
		"""
		allure.dynamic.title("Clear to be pressed multiple times test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Clear to be pressed multiple times"):
			self.enter_number(123456789)
			self.app.del_btn.tap()
			self.app.del_btn.tap()
			self.app.del_btn.tap()
			assert self.app.screen_result.label == ''

	def test_clear_after_inserting_a_many_digit_floating_point_number(self):
		"""
		Should be able to clear after inserting a many digit floating point number
		1234.56789 C -> 0
		:return:
		"""
		allure.dynamic.title("Clear after inserting a many digit floating point number test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Clear after inserting a many digit floating point number"):
			self.enter_number(1234.56789)
			self.app.del_btn.tap()
			assert self.app.screen_result.label == ''

	def test_clear_after_inserting_a_negative_many_digit_floating_point_number(self):
		"""
		Should be able to clear after inserting a negative many digit floating point number
		-1234.56789 C -> 0
		:return:
		"""
		allure.dynamic.title("Clear after inserting a negative many digit floating point number test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Clear after inserting a negative many digit floating point number"):
			self.enter_number(-1234.56789)
			self.app.del_btn.tap()
			assert self.app.screen_result.label == ''

	def test_clear_after_inserting_a_large_negative_integer(self):
		"""
		Should be able to clear after inserting a large negative intgeger
		-123456789 C -> 0
		:return:
		"""
		allure.dynamic.title("Clear after inserting a large negative integer test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Clear after inserting a large negative integer"):
			self.enter_number(-123456789)
			self.app.del_btn.tap()
			assert self.app.screen_result.label == ''

	def test_clear_after_inserting_a_large_integer(self):
		"""
		Should be able to clear after inserting a large integer
		123456789 C -> 0
		:return:
		"""
		allure.dynamic.title("Clear after inserting a large integer test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Clear after inserting a large integer"):
			self.enter_number(123456789)
			self.app.del_btn.tap()
			assert self.app.screen_result.label == ''


