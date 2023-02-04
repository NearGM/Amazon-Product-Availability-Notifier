# Amazon Product Availability Notifier
This script checks the availability of a product on Amazon and sends notifications of the availability status using Selenium and notify2.

## Prerequisites

    selenium
    notify2


## Usage

1.    Clone the repository
2.    Replace the product URL in amazon-product-availability-notifier.py
```sh
def check_product_availability():
    # You need to change the url to the product you want 
    product_url = 'https://www.amazon.com/dp/B07WY7TTL5/ref=nosim?tag=americanapparel.com-20&th=1&psc=1'
```
4.    Run the script

## Explanation

The script uses Selenium to open the product page in a headless browser and locate the availability element by its ID. It checks the availability status and sends notifications using the notify2 library. The status notifications include temporarily out of stock, currently unavailable, in stock, and availability not found. The script quits the webdriver after sending the notification.
