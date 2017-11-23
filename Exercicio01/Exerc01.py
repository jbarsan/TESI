from selenium import webdriver

"""
Busque site com os elementos relacionados a algum valor financeiro ou e-commerce:
a) Estude a estrutura da exibição de dados;
b) Manipule buscas simples via web driver;
c) Obtenha informações a respeito de algum produto.
"""

URL = 'https://www.kabum.com.br'
CONSULTA = 'placa de video'

browser = webdriver.Chrome('chromedriver')
browser.get(URL)
pesquisa = browser.find_element_by_css_selector('.sprocura')
pesquisa.send_keys(CONSULTA)
pesquisa.submit()



