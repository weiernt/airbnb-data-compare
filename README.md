# Airbnb-data-compare
Outputs relative standing of user compared to others in Melbourne.

Uses data openly obtained from http://insideairbnb.com/get-the-data.html. Link needs to be manually changed if data is updated, currently using May 2020 dataset. This dataset will be accessed with a http request, and saved locally in the same directory as main.py, and will be saved as local.csv.

Script sums up the unique host_ids' total reviews on each unique listing id, then sorts this list of tuples. The input user from the input url is then compared to this sorted list to see how the user's number of reviews stands relative to the list.

Note that the terminal has to be in the same directory as main.py


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
