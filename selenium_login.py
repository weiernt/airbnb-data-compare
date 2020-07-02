#
from bs4 import BeautifulSoup
import time
import get_input_reviews
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

DUMMY_EMAIL = r"struntio1930@einrot.com" # expires in 24hours from 14:11
DUMMY_PASSWORD = r"adminadminadmin01"

TEST_PRIVATE_PROFILE_URL = r"https://www.airbnb.com.au/users/show/7468324"

#TODO:
# current issue is CAPTCHA when logging in.
# otherwise everything works fine

if __name__ == "__main__":

    driver = webdriver.Firefox()
    driver.get(TEST_PRIVATE_PROFILE_URL)

    useEmailLogin = driver.find_element_by_class_name("_bc4egv")
    ActionChains(driver).click(useEmailLogin).perform()

    idLoginElem = driver.find_element_by_id("email")
    idLoginElem.clear()
    idLoginElem.send_keys(DUMMY_EMAIL)

    passwordLoginElem = driver.find_element_by_id("password")
    passwordLoginElem.clear()
    passwordLoginElem.send_keys(DUMMY_PASSWORD)

    passwordLoginElem.send_keys(Keys.ENTER)

    # wait a while to load the page
    time.sleep(10)

    html = driver.page_source

    print("n_reviews from this site:")
    print(get_input_reviews.get_input_reviews_html(html))

    # assert "No results found." not in driver.page_source
    driver.quit()