from selenium import webdriver
browser = webdriver.Chrome('chromedriver')
browser.get('https://google.com')
browser.execute_script('alert("Oi, eu sou o Goku!")')
browser.save_screenshot('print.png')

ent = browser.find_element_by_css_selector('#lst-ib')
ent.send_keys('João Carlos Barsan')
ent.clear()
browser.close()