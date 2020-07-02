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

def perform_login(url):
    """Opens web browser to login to airbnb using a dummy email and password.
       then returns the html for the page after login"""
    driver = webdriver.Firefox()
    driver.get(url)

    # class name corresponds to button for email login
    useEmailLoginElem = driver.find_element_by_class_name("_bc4egv")
    ActionChains(driver).click(useEmailLoginElem).perform()

    idLoginElem = driver.find_element_by_id("email")
    idLoginElem.clear()
    idLoginElem.send_keys(DUMMY_EMAIL)

    passwordLoginElem = driver.find_element_by_id("password")
    passwordLoginElem.clear()
    passwordLoginElem.send_keys(DUMMY_PASSWORD)

    passwordLoginElem.send_keys(Keys.ENTER)

    time.sleep(10) #short delay to let html load

    page_html = driver.page_source
    driver.quit()

    return page_html


if __name__ == "__main__":

    # wait a while to load the page
    time.sleep(10)

    html = perform_login(TEST_PRIVATE_PROFILE_URL)

    print("n_reviews from this site:")
    print(get_input_reviews.get_input_reviews_html(html))

    # assert "No results found." not in driver.page_source
    # driver.quit()

    #id = "recaptcha-audio-button" type button
    # id = "recaptcha-anchor"
    # download link <a> = "rc-audiochallenge-tdownload-link"