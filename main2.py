from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome()
driver.get('https://id.carousell.com/categories/photography-6')
WebDriverWait(driver, 20)

# while True:
#     try:
#         WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, '#main > div.D_aHi > div > div.D_aHu > main > div > button'))).click()
#         time.sleep(2)
#     except Exception as e:
#         print(e)
#         break

photography = []
data = driver.find_elements(By.CSS_SELECTOR, 'main > div > div > div > div > div.D_os')
for i in data:
    judul = i.find_element(By.CSS_SELECTOR, 'p.D_jj.D_gU.D_jk.D_jn.D_jq.D_jt.D_jv.D_jr.D_jg')
    image = i.find_element(By.CSS_SELECTOR, 'main > div > div > div > div > div.D_os > a:nth-child(2) > div.D_o_ > div > div > img').get_dom_attribute('src')
    toko = i.find_element(By.CSS_SELECTOR, 'a.D_ow.D_iJ > div.D_oz > p').text
    harga = i.find_element(By.CSS_SELECTOR, 'a:nth-child(2) > div.D_oK > p').text
    kondisi = i.find_element(By.CSS_SELECTOR, 'a:nth-child(2) > p:nth-child(4)').text
    print(image)

driver.quit()
