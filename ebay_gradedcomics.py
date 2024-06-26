import re
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def scrape_comic_prices(comic_name):
    # Setup the driver
    options = Options()
    options.headless = True  # Optional: if you don't want the browser to open up
    driver = webdriver.Chrome(options=options)

    try:
        # Navigate to the eBay search page
        driver.get('https://www.ebay.com')
        time.sleep(5)  # Wait for the page to load

        # Search for the specified comic
        search_box = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')  # Adjust selector if necessary
        search_box.send_keys(comic_name + " graded")
        search_box.send_keys(Keys.ENTER)
        time.sleep(5)  # Wait for search results to load

        # Collect data
        comics = []
        listings = driver.find_elements(By.CSS_SELECTOR, '.s-item')  # Adjust selector based on eBay’s layout
        for listing in listings:
            title = listing.find_element(By.CSS_SELECTOR, '.s-item__title').text  # Adjust selector if necessary
            if 'graded' in title.lower():  # Check if 'graded' is in the title
                price = listing.find_element(By.CSS_SELECTOR, '.s-item__price').text  # Adjust selector if necessary
                grade_match = re.search(r'(CGC|NM|VF|VG|G|PG)\s*(?:graded\s*)?(\d+\.\d+)|(\d+\.\d+)\s*(?:graded\s*)?(CGC|NM|VF|VG|G|PG)', title, re.I)
                url = listing.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
                if grade_match:
                    # Reconstruct the grade string if elements are found out of order
                    grade = grade_match.group(1) + ' ' + grade_match.group(2) if grade_match.group(1) else grade_match.group(4) + ' ' + grade_match.group(3)
                else:
                    grade = 'Grade not specified'
                if 'graded' in title.lower():
                    comics.append({'title': title, 'url': url, 'grade': grade, 'price': price})

                    # Write to CSV
        with open('comics.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for comic in comics:
                writer.writerow([comic['title'], comic['url'], comic['grade'], comic['price']])

    finally:
        driver.quit()

# User input
comic_name = input("Enter the name of the comic you are interested in: ")
scrape_comic_prices(comic_name)
