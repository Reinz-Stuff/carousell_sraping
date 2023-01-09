from flask import Flask, render_template
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

app = Flask(__name__)


@app.route('/')
def myphotography():
    driver = webdriver.Chrome()
    driver.get('https://id.carousell.com/categories/photography-6')
    driver.maximize_window()

    j = 1
    while True:
        # Scroll down
        print(f"scrolling down...{j}")
        bottom = False
        a = 0
        while not bottom:
            new_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script(f"window.scrollTo(0, {a});")
            if a > new_height:
                bottom = True
            a += 10
        j += 1

        try:
            # Wait all elements to appear
            images = driver.find_elements(By.XPATH,
                                          '//*[@id="main"]/div[2]/div/div[5]/main/div/div/div/div/div[1]/a[2]/div[1]/div/div/img')

            # if all 48 element loaded
            if len(images) == 48:
                print(f"{len(images)} product detail found...!")

                # fetch each element attribute into one dict/json
                print("scraping product detail...")
                judul = driver.find_elements(By.XPATH,
                                             '//*[@id="main"]/div[2]/div/div[5]/main/div/div/div/div/div[1]/a[2]/p[1]')
                image = driver.find_elements(By.XPATH,
                                             '//*[@id="main"]/div[2]/div/div[5]/main/div/div/div/div/div[1]/a[2]/div[1]/div/div/img')
                harga = driver.find_elements(By.XPATH,
                                             '//*[@id="main"]/div[2]/div/div[5]/main/div/div/div/div/div[1]/a[2]/div[2]/p')
                urls = driver.find_elements(By.XPATH, '//*[@id="main"]/div[2]/div/div[5]/main/div/div/div/div/div[1]/a[2]')

                product = zip(judul, image, harga, urls)
                media = 'https://id.carousell.com'

                return render_template('index.html', product=product, media=media)
            else:
                print(f"{48 - len(images)} product detail not loaded...rescrolling")
                pass

        except NoSuchElementException:
            print("cannot find all image")
            break


if __name__ == '__main__':
    app.run(port=5002, debug=True)
