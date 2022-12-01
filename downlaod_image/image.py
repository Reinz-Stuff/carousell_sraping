import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://id.carousell.com/categories/photography-6')
driver.maximize_window()

bottom = False
a = 0
while not bottom:
    new_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script(f"window.scrollTo(0, {a});")
    if a > new_height:
        bottom = True
    a += 5

data = driver.find_elements(By.CSS_SELECTOR, 'main > div > div > div > div > div.D_uO')
judul = 1
for i in data:
    j = str(judul)
    image = i.find_element(By.CSS_SELECTOR, 'a:nth-child(2) > div.D_uW > div > div > img').get_dom_attribute('src')

    with open('images/' + j + '.jpg', 'wb') as f:
        img = requests.get(image)
        f.write(img.content)
    judul += 1
driver.quit()
