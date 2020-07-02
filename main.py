from bs4 import BeautifulSoup
import requests
import os
import sys
import csv
import urllib.request
from collections import defaultdict

import get_input_reviews 

AIRBNB_DATA_URL = r"http://data.insideairbnb.com/australia/vic/melbourne/2020-05-13/visualisations/listings.csv"


if __name__ == "__main__":
    if len(sys.argv) == 1 :
        # Requires input url
        print(f"Usage: {sys.argv[0]} [airbnb_url]\n")
        print(r"Input airbnb user profile, ie: 'https://www.airbnb.com/users/show/xxxxxxx' ", 
               "\nThis will then be compared with other hosts in Melbourne, Victoria")
        sys.exit(1)
    
    if os.path.isfile("./local.csv") == False:
        print("Fetching Airbnb data...")
        # Obtain csv data for Melbourne airbnb listings
        csv_http = urllib.request.urlopen(AIRBNB_DATA_URL)

        # Save the data from csv_http into a local csv copy
        with open(r"./local.csv", "w", encoding="utf-8") as localcsv:
            localcsv.write(csv_http.read().decode("utf-8"))

    # remember to always open, read, write with explicit de/encoding="utf-8"

    f = open(r"./local.csv", encoding="utf-8")
    csvfile = csv.DictReader(f)

    counter = defaultdict(int) # counter for each unique host_id

    # get number of reviews from the input URL provided
    n_input_user_reviews = get_input_reviews.get_input_reviews(sys.argv[1])

    # adds number of reviews to each unique host_id
    for csv_row in csvfile:
        counter[csv_row["host_id"]] += int(csv_row["number_of_reviews"])

    # Sort the dict by second value, which is the total number of reviews
    list_counter = sorted(counter.items(), key=lambda k_v: k_v[1])

    # just do simple analysis by finding the index of the input user's number of reviews
    # relative to the sorted list of hosts with their total number of reviews.
    i=0
    for entry in list_counter:
        i+=1
        if n_input_user_reviews <= entry[1]:
            break


    percent = i/len(list_counter)*100
    print(f"This user is {percent} %")
    print(f"    and is in the top {100 - percent:.2f} % of Melbourne hosts based on number of reviews.")
    
    f.close()
    sys.exit(0)



