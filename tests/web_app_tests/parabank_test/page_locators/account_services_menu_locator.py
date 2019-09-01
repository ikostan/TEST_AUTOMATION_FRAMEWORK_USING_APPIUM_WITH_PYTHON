"""Account Services Menu Locator Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.common.by import By


class AccountServicesMenuLocator:
	"""
	Holds all relevant locators for any page web elements.
	Each locator is a tuple.
	Separate the locator strings from the place where they are being used.
	"""

	WELCOME_MESSAGE = (By.XPATH, '//*[@id="leftPanel"]/p')

	ACCOUNT_SERVICES_HEADER = (By.XPATH, '//h2[contains(text(),"Account Services")]')

	OPEN_NEW_ACCOUNT = (By.XPATH, '//*[@id="leftPanel"]/ul/li[1]/a[text()="{}"]'.format(
		BankAccountContent.ACCOUNT_SERVICES_MENU['menu_items']['open_new_account']['text']))

	ACCOUNTS_OVERVIEW = (By.XPATH, '//*[@id="leftPanel"]/ul/li[2]/a[text()="{}"]'.format(
		BankAccountContent.ACCOUNT_SERVICES_MENU['menu_items']['account_overview']['text']))

	TRANSFER_FUNDS = (By.XPATH, '//*[@id="leftPanel"]/ul/li[3]/a[text()="{}"'.format(
		BankAccountContent.ACCOUNT_SERVICES_MENU['menu_items']['transfer_funds']['text']))

	BILL_PAY = (By.XPATH, '//*[@id="leftPanel"]/ul/li[4]/a[text()="{}"'.format(
		BankAccountContent.ACCOUNT_SERVICES_MENU['menu_items']['bill_pay']['text']))

	FIND_TRANSACTIONS = (By.XPATH, '//*[@id="leftPanel"]/ul/li[5]/a[text()="{}"'.format(
		BankAccountContent.ACCOUNT_SERVICES_MENU['menu_items']['find_transactions']['text']))

	UPDATE_CONTACT_INFO = (By.XPATH, '//*[@id="leftPanel"]/ul/li[6]/a[text()="{}"'.format(
		BankAccountContent.ACCOUNT_SERVICES_MENU['menu_items']['update_info']['text']))

	REQUEST_LOAN = (By.XPATH, '//*[@id="leftPanel"]/ul/li[7]/a[text()="{}"'.format(
		BankAccountContent.ACCOUNT_SERVICES_MENU['menu_items']['request_loan']['text']))

	LOG_OUT = (By.XPATH, '//a[text()="{}"]'.format(
		BankAccountContent.ACCOUNT_SERVICES_MENU['menu_items']['log_out']['text']))
