from bs4 import BeautifulSoup
import requests
import re
import selenium_login

def get_input_reviews(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    if ("Log In" in soup.title.text):
        # Somehow in a login page, so do login
        print("Logging in with dummy account...")
        html = selenium_login.perform_login(url)
        return get_input_reviews_html(html)
    
    return get_input_reviews_html(r.content)


def get_input_reviews_html(html_source):
    regex = re.compile(r"[0-9]+ reviews")
    n_reviews = 0

    soup = BeautifulSoup(html_source, "html.parser")

    for entry in soup.findAll("div", {"class": "_czm8crp"}):
        try:
            # print(entry.contents[0].text)
            m = regex.match(entry.contents[0].text)

            # m.group() == True means found a match for regex
            if m.group():
                # print(m)
                n_reviews = int(m.group().split()[0])
                print(f"n_reviews = {n_reviews} ")
                return n_reviews
        except:
            # entry.contents[0] does not exist
            pass

    # should always be able to find the regex in the website
    raise ValueError("Failed to find reviews regex, likely used wrong url or airbnb.com changed") 




if __name__ == "__main__":
    # purely for testing here
    URL = r"https://www.airbnb.com/users/show/99824610"
    get_input_reviews(URL)
