import requests
from bs4 import BeautifulSoup

# The URL of the targeted webpage
URL = "https://www.konzolvilag.hu/xboxseries/xbox-series-x-1tb-digital-edition-white-plugnelkul"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def check_website():
    print("Trying to connect to the website...")

    # Sending a GET request to the website
    response = requests.get(URL, headers=HEADERS)

    # If the response status code is 200, the connection was successful
    if response.status_code == 200:
        print("Awesome! Successfully fetched the website content!")

        #Handing over the download HTML content to BeautifulSoup for parsing
        soup = BeautifulSoup(response.text, 'html.parser')

        #Finding the first 'div'  element with the class 'now'
        price_element = soup.find('div', class_='now')

        #Checking if the element was found
        if price_element:
            #Extracting the next and removing unnecessary whitespace
            raw_price = price_element.text.strip()
            print(f"Boom, found the price: {raw_price}")
        else:
            print("Couldn't find the price. The website structure muight have changed.")


    else:
        print(f"Oops, something went wrong. Status code: {response.status_code}")

if __name__ == "__main__":
    check_website()