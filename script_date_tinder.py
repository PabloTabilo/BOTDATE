from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

path = "/Users/ticnow/Downloads/chromedriver_2"
number = ""


class Tinder_profile():
	def __init__(self, url):
		self.url = url
		self.driver = webdriver.Chrome(path)
		self.driver.get(self.url)

	def conectar_telefono(self):
		xpath_button = "//button[@class='button Lts($ls-s) Z(0) CenterAlign Mx(a) Pos(r) Cur(p) Tt(u) Bdrs(100px) Px(48px) Px(40px)--s Py(0) Mih(54px) button--outline Bdw(2px) Bds(s) Trsdu($fast) Bdc($c-secondary) C($c-secondary) Bdc($c-base):h C($c-base):h Bdc($c-base):f C($c-base):f Bdc($c-base):a C($c-base):a Fw($semibold) focus-button-style Mb(20px)--ml W(100%)--ml W(100%)--s Fz(4vw)--s']"
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

        contenedor_codes = "//input[@class='Fz($m) Va(m) Py(8px) Bdrs(4px)--ml Bgc($c-divider-lite)--ml Px(8px)--ml BdB--s Bdrs(0)--s Bdbc($c-secondary)--s Px(4px)--s Sq(48px) Sq(40px)--s Ta(c) Fw($bold) Mend(6px)']"
            
        contador = 0
        for val_i in contenedor_codes:
            val_i.send_keys(caracteres_code[contador])
            contador += 1

        xpath_button_final = "//button[@class='button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(54px) Pos(r) Ov(h) C(#fff) Bg($c-pink):h::b Bg($c-pink):f::b Bg($c-pink):a::b Trsdu($fast) Trsp($background) Bg($primary-gradient) button--primary-shadow StyledButton Fw($semibold) focus-button-style My(20px) My(12px)--xs Maw(315px) W(100%) Ell']"

        button_final = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, xpath_button_final)))
        button_final.click()

    

if __name__ == "__main__":
	tinder_link = "https://tinder.com/"
	badoo_instance = Badoo_profile(badoo_link)
    
