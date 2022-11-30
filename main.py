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
    a += 10

photography = []
data = driver.find_elements(By.CSS_SELECTOR, 'main > div > div > div > div > div.D_os')
for i in data:
    judul = i.find_element(By.CSS_SELECTOR, 'p.D_jj.D_gU.D_jk.D_jn.D_jq.D_jt.D_jv.D_jr.D_jg').text
    image = i.find_element(By.CSS_SELECTOR, 'a:nth-child(2) > div.D_o_ > div > div > img').get_dom_attribute('src')
    toko = i.find_element(By.CSS_SELECTOR, 'a.D_ow.D_iJ > div.D_oz > p').text
    harga = i.find_element(By.CSS_SELECTOR, 'a:nth-child(2) > div.D_oK > p').text
    kondisi = i.find_element(By.CSS_SELECTOR, 'a:nth-child(2) > p:nth-child(4)').text

    print(judul, harga, image)

    list_barang = {
        'judul': judul,
        'image': image,
        'toko': toko,
        'harga': harga,
        'kondisi': kondisi
    }
    photography.append(list_barang)

print(photography)

driver.quit()
