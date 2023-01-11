# Carousell Scraping
This package utilizes a web scraping method to collect data from the carousell website, and converts it into various formats such as JSON, CSV and Excel files. The package also includes the functionality to create a web application using the collected data, allowing users to view and interact with the results in a user-friendly format.

## HOW IT WORK?
This package utilizes Selenium to scrape product information from [carousell](https://id.carousell.com/categories/photography-6) and uses pandas to organize the data into a DataFrame. The DataFrame can then be saved in various formats such as JSON, CSV, and Excel. The package also includes a feature to create a web application using Flask, which allows the scraped data to be viewed and interacted with through a web interface. The output files will be saved in the current working directory.

## HOW TO USE
To utilize the carousell_scraping script, please follow these steps:

1. Open a terminal window.
2. Run the command "py automate.py" and press Enter.
3. The script will execute and automatically scrape data from the specified URL, saving the results in a folder called "Extraction" and "downloaded_image".
4. Use the local server given to view the results in the web app format created by Flask

## Author
Fauzi Kurniawan
