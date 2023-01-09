import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


def data_extraction():
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
                photography = []
                j = 1
                for a, b, c in zip(judul, image, harga):
                    title = a.text
                    img = b.get_dom_attribute('src')
                    price = c.text
                    dicts = {
                        'Nama Produk': title,
                        'Gambar Produk': img,
                        'Harga Produk': price
                    }
                    photography.append(dicts)

                    print(f"get product detail....{j}")
                    j += 1

                # writing result to files
                print("writing variable into file...")
                df = pd.DataFrame(photography)

                # Write the DataFrame to a JSON file
                df.to_json("result.json", orient="records")
                print(f"JSON file created....!")

                # Write the DataFrame to a CSV file
                df.to_csv("result.csv", index=False)
                print(f"CSV file created....!")

                # Write the DataFrame to a excel file
                df.to_excel("result.xlsx", index=False)
                print(f"excel file created....!")

                print("process finished!")
                break
            else:
                print(f"{48 - len(images)} product detail not loaded...rescrolling")
                pass

        except:
            print("cannot find all image")
            break



if __name__ == '__main__':
    data_extraction()
