import json
import openai
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def generate_personalized_message(details):
    prompt = f"I am interested in {details['Title']} listed for sale. {details['Additional Info']}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def check_offer_options(comic_details):
    driver = webdriver.Chrome()
    driver.get(comic_details['URL'])
    time.sleep(5)
    
    try:
        personalized_message = generate_personalized_message(comic_details)

        try:
            make_offer_button = driver.find_element(By.ID, 'boBtn_btn')
            make_offer_button.click()
            time.sleep(2)
            offer_input = driver.find_element(By.ID, 'boPrice_inp')
            offer_input.send_keys(str(comic_details['Best Offer']))
            message_input = driver.find_element(By.ID, 'message_input')  # Update ID based on the actual element
            message_input.send_keys(personalized_message)
            # Submit the offer
        except:
            contact_seller_link = driver.find_element(By.LINK_TEXT, 'Contact seller')
            contact_seller_link.click()
            message_input = driver.find_element(By.ID, 'message_input')  # Update ID based on the actual element
            message_input.send_keys(personalized_message)
            # Send the message

    finally:
        driver.quit()

if __name__ == "__main__":
    with open('offer_details.json', 'r') as file:
        comic_details = json.load(file)
    check_offer_options(comic_details)