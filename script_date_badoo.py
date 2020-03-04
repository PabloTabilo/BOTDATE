from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

path = "/Users/ticnow/Downloads/chromedriver_2"
user = ""
password = ""


class Badoo_profile():
	def __init__(self, url):
		self.url = url
		self.driver = webdriver.Chrome(path)
		self.driver.get(self.url)

	def conectate_inicial(self):
		xpath_conectate = "//div[@class='header-sign-in__button']/a"
		ahref_conectate = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, xpath_conectate)))
		ahref_conectate.click()

	def login(self):
		xpath_email = "//input[@name='email']"
		xpath_pass = "//input[@name='password']"

		inputEmail = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH, xpath_email)))
		inputPass = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH, xpath_pass)))

		inputEmail.send_keys(user)
		inputPass.send_keys(password)

		buttonElement = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
		buttonElement.click()

	def click_button(self):
		xpath_badoo = "//div[@data-choice='yes']"
		heart_badoo = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, xpath_badoo)))
		heart_badoo.click()

	def rare_element(self):
		xpath_span_close = "//span[@class='p-link js-ovl-close']"
		span_close = WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located((By.XPATH, xpath_span_close)))
		span_close.click()

	def notify(self):
		xpath_notify = "//div[@class='btn btn--monochrome js-chrome-pushes-deny']"
		notify_close = WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located((By.XPATH, xpath_notify)))
		notify_close.click()

	def noVotes(self):
		xpath_noVotes = "//div[@class='btn js-ovl-action']"
		noVotesElement = WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located((By.XPATH, xpath_noVotes)))
		noVotesElement.click()

if __name__ == "__main__":
	tinder_link = "https://tinder.com/"
	badoo_link = "https://badoo.com/"

	badoo_instance = Badoo_profile(badoo_link)
	time.sleep(2)
	try:
		badoo_instance.conectate_inicial()
	except :
		print("No tiene conectate_inicial")
	badoo_instance.login()

	try:
		badoo_instance.rare_element()
	except :
		print("No tenemos span raro")

	contador = 0
	while True:
		contador += 1

		# Se acabo los votos
		try:
			badoo_instance.noVotes()
		except :
			time.sleep(0.5)

		# span raro
		try:
			badoo_instance.rare_element()
		except :
			time.sleep(0.5)

		# notificacion
		try:
			badoo_instance.notify()
			print("Encontrado un notify!")
		except :
			time.sleep(0.5)

		# dando like
		badoo_instance.click_button()
		print("Dado click!!")
		if contador > 400:
			break

	print("Bot muerto!")
