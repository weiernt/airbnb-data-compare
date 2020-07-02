# Airbnb-data-compare

Compares relative standing of airbnb user profiles, by comparing their number of reviews, available publically. This is compared to the data obtained from http://insideairbnb.com/ . Currently uses the May 2020 dataset.

This only compares with data from listings in Melbourne, Australia.

Note that requires the current working directory to be in the main folder (same directory as `main.py`) to work properly.

# Usage
```
py main.py https://www.airbnb.com/users/show/xxxxxxxxxxxxxx
```
Where `xxxxxxxx` represents the airbnb user profile ID.

# Dependencies
- BeautifulSoup4 (4.9.0)
- Requests (2.22.0)
- Selenium (3.141.0)

Versions listed at time of building
