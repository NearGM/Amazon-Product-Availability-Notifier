import notify2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


def check_product_availability():
    # You need to change the url to the product you want
    product_url = 'https://www.amazon.com/dp/B07WY7TTL5/ref=nosim?tag=americanapparel.com-20&th=1&psc=1'
    if "amazon" not in product_url:
        print("Invalid URL. Please enter an Amazon URL.")
        notify2.init("Amazon Product Availability")
        n = notify2.Notification("Amazon Product Availability", "Invalid URL. Please enter an Amazon URL.")

    print('Checking for the Amazon Product...')
    notify2.init("Amazon Product Availability")
    n = notify2.Notification("Amazon Product Availability", "Checking for the Amazon product...⏳⌛️")
    n.show()

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)
    driver.get(product_url)
    try:
        availability_element = driver.find_element(By.ID, 'availability')
        availability = availability_element.text
        if 'Temporarily out of stock' in availability:
            print('The product is temporarily out of stock')
            notify2.init("Amazon Product Availability")
            n = notify2.Notification("Amazon Product Availability", "The product is temporarily out of stock. You'll need to wait a bit more... ⏳⌛️")
            n.show()
        elif 'Currently unavailable' in availability:
            print('The product is currently unavailable')
            notify2.init("Amazon Product Availability")
            n = notify2.Notification("Amazon Product Availability", "The product is currently unavailable. You'll need to wait a bit more...⏳⌛️")
            n.show()
        elif 'In Stock' in availability:
            print('The product is in stock')
            notify2.init("Amazon Product Availability")
            n = notify2.Notification("Amazon Product Availability", "The product is in stock. Go get it now !! 💻💸📦📬")
            n.show()
        else:
            print(f'Availability: {availability}')
            notify2.init("Amazon Product Availability")
            n = notify2.Notification("Amazon Product Availability", f'Availability: {availability}')
            n.show()
    except:
        print("availability not found")
        notify2.init("Amazon Product Availability")
        n = notify2.Notification("Amazon Product Availability", "Availability not found")
        n.show()

    driver.quit()



if __name__ == "__main__":
    check_product_availability()

