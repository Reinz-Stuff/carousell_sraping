import json
import os
import requests


def image_extraction():
    with open('Extraction/result.json') as f:
        data = json.load(f)

    try:
        os.makedirs('downloaded_image')
    except FileExistsError:
        print(f'folder already exists.')

    j = 1
    for image in data:
        img = image['Gambar Produk']
        response = requests.get(img)
        open(f"downloaded_image/product__{j}.jpg", "wb").write(response.content)

        print(f"image {j} downlaoded!")
        j += 1


if __name__ == '__main__':
    image_extraction()
