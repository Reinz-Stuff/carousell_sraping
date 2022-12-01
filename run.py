from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.common.by import By

app = Flask(__name__,
            static_folder='carousell_scraping')


# app._static_folder = '/static'


@app.route('/')
def home():
    return render_template('index.html')


def camera_list():
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

    data = driver.find_elements(By.CSS_SELECTOR, 'main > div > div > div > div > div.D_os')
    for i in data:
        judul = i.find_element(By.CSS_SELECTOR, 'p.D_jj.D_gU.D_jk.D_jn.D_jq.D_jt.D_jv.D_jr.D_jg').text
        image = i.find_element(By.CSS_SELECTOR, 'a:nth-child(2) > div.D_o_ > div > div > img').get_dom_attribute('src')
        harga = i.find_element(By.CSS_SELECTOR, 'a:nth-child(2) > div.D_oK > p').text

    return render_template('index.html', titles=data)


if __name__ == '__main__':
    app.run(debug=True)
