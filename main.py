from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://id.carousell.com/categories/photography-6")
driver.quit()

# soup = BeautifulSoup(driver, 'html.parser')
# page = soup.find(attrs='D_gc M_KN D_aHA')
# content = page.find_all(attrs='D_iJ')
# title = soup.find_all(attrs='D_jj M_he D_gS M_fi D_jk M_hf D_jn M_hi D_jp M_hk D_jt M_ho D_jw M_hr D_jg')
# title.pop(0 - 1)
# image = soup.find_all(attrs='D_uc D_ue')
# print(soup)
#
# # for i in title:
# #     print(i.text)
