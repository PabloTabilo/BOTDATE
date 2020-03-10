from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import os
import time


path = "/Users/ticnow/Downloads/chromedriver_2"
#path = "C:/Users/pablo/Downloads/chromedriver.exe"
number = ""


class Tinder_profile():
	def __init__(self, url):
		self.url = url
		self.driver = webdriver.Chrome(path)
		self.driver.get(self.url)

	def conectar_telefono(self):
		xpath_button = "//button[@aria-label='Inicia sesión con tu teléfono']"
		button_fono = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, xpath_button)))
		button_fono.click()

		xpath_input = "//input[@name='phone_number']"
		button_fono = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, xpath_input)))
		button_fono.send_keys(number)

		xpath_continue = "//button[@class='button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(54px) Pos(r) Ov(h) C(#fff) Bg($c-pink):h::b Bg($c-pink):f::b Bg($c-pink):a::b Trsdu($fast) Trsp($background) Bg($primary-gradient) button--primary-shadow StyledButton Fw($semibold) focus-button-style My(20px) My(12px)--xs Maw(315px) W(100%) Ell']"
		button_continue = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, xpath_continue)))
		button_continue.click()

		print("Dame el codigo del telefono: ")
		codigo_fono = input("Escribe: ")
		caracteres_code = codigo_fono.split()

		x_path_contenedor_codes = "//input[@class='Fz($m) Va(m) Py(8px) Bdrs(4px)--ml Bgc($c-divider-lite)--ml Px(8px)--ml BdB--s Bdrs(0)--s Bdbc($c-secondary)--s Px(4px)--s Sq(48px) Sq(40px)--s Ta(c) Fw($bold) Mend(6px)']"
		contenedor_codes = self.driver.find_elements_by_xpath(x_path_contenedor_codes)
		
		contador = 0
		for val_i in contenedor_codes:
			try:
				val_i.send_keys(caracteres_code[contador])
				contador += 1
			except:
				break

		time.sleep(3)
		try:
			xpath_button_final = "//button[@class='button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(54px) Pos(r) Ov(h) C(#fff) Bg($c-pink):h::b Bg($c-pink):f::b Bg($c-pink):a::b Trsdu($fast) Trsp($background) Bg($primary-gradient) button--primary-shadow StyledButton Fw($semibold) focus-button-style My(20px) My(12px)--xs Maw(315px) W(100%) Ell']"
			button_final = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, xpath_button_final)))
			button_final.click()
		except:
			xpath_button_final = "//div[@class='Ta(c) Expand Mx(a)']/button"
			button_final = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, xpath_button_final)))
			button_final.click()

	def startButtons(self):
		# Permitir ubicacion
		xpath_permitir = "//button[@aria-label='Permitir']"
		button_permitir = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, xpath_permitir)))
		button_permitir.click()

		# Recibir notificaciones?
		xpath_notify = "//button[@aria-label='No me interesa']"
		button_notify = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, xpath_notify)))
		button_notify.click()

	def likeButton(self):
		xpath_like = "//div[@class='Mx(a) Fxs(0) Sq(70px) Sq(60px)--s']"
		button_like = self.driver.find_elements_by_xpath(xpath_like)[1]
		button_like.click()

if __name__ == "__main__":
	tinder_link = "https://tinder.com/"
	tinder_instance = Tinder_profile(tinder_link)
	# Conectar el telefono
	tinder_instance.conectar_telefono()

	# Botones iniciales
	tinder_instance.startButtons()

	contador = 0
	while True:
		contador += 1
		if contador == 1:
			time.sleep(4)
		tinder_instance.likeButton()
		time.sleep(0.9)
    
