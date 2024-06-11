import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def check_offer_options(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    
    try:
        try:
            make_offer_button = driver.find_element(By.ID, 'boBtn_btn')
            print("Best Offer option is available.")
        except:
            contact_seller_link = driver.find_element(By.LINK_TEXT, 'Contact seller')
            contact_seller_link.click()
            print("Navigated to the Contact Seller page.")

    finally:
        driver.quit()

if __name__ == "__main__":
    with open('selected_comic_info.json', 'r') as file:
        selected_comic = json.load(file)
    check_offer_options(selected_comic['URL'])
