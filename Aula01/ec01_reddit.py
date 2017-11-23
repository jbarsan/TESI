from selenium import webdriver
browser = webdriver.Chrome('chromedriver')
browser.get('https://reddit.com')
titles = browser.find_elements_by_css_selector('.title .may-blank')

for i in range(3):
    print('Página ', i + 1)
    for t in titles:
        print(t.text)
    print('-------------------------')

    proximo = browser.find_element_by_css_selector('.next-button a')
    proximo.click()