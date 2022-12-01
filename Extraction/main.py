from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

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
    a += 10

data = driver.find_elements(By.CSS_SELECTOR, 'main > div > div > div > div > div.D_uO')

file = open('hasilextraction.csv', 'w', newline='')
write = csv.writer(file)
headers = ['Produk', 'Nama Toko', 'Harga', 'Kondisi']

photography = []
for i in data:
    judul = i.find_element(By.CSS_SELECTOR, 'a:nth-child(2) > p.D_sV.D_so.D_sW.D_sZ.D_tc.D_tg.D_ti.D_te.D_tu').text
    image = i.find_element(By.CSS_SELECTOR, 'a:nth-child(2) > div.D_uW > div > div > img').get_dom_attribute('src')
    toko = i.find_element(By.CSS_SELECTOR, 'a.D_uS.D_uo > div.D_uV > p').text
    harga = i.find_element(By.CSS_SELECTOR, 'a:nth-child(2) > div.D_vh > p').text
    kondisi = i.find_element(By.CSS_SELECTOR, 'a:nth-child(2) > p:nth-child(4)').text

    file = open('hasilextraction.csv', 'a', newline='', encoding='utf-8')
    write = csv.writer(file)
    write.writerow([judul, toko, harga, kondisi])
    file.close()
print('csv created!')


driver.quit()
