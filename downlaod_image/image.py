import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://id.carousell.com/categories/photography-6')
driver.maximize_window()

j = 1
while True:
    # Scroll down
    print(f"scrolling down...{j}")
    driver.execute_script("window.scrollTo(0, 0);")
    bottom = False
    a = 0
    while not bottom:
        new_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script(f"window.scrollTo(0, {a});")
        if a > new_height:
            bottom = True
        a += 10
    driver.execute_script("window.scrollTo(0, 0);")
    j += 1

    try:
        # Wait all elements to appear
        images = driver.find_elements(By.XPATH,  '//img[@class="D_vo D_vl D_Xz"]')
        if len(images) == 48:
            print(f"{len(images)} image found...!")
            j = 1
            for image in images:
                img = image.get_dom_attribute('src')
                response = requests.get(img)
                open(f"images/product__{j}.jpg", "wb").write(response.content)

                print(f"image {j} downlaoded!")
                j += 1
            break
        else:
            print(f"{48 - len(images)} image not loaded...rescrolling")
            pass

    except:
        print("cannot find all image")
        break
