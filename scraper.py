from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Configure Selenium WebDriver
def setup_driver():
    options = Options()
    options.add_argument("--headless")  # Run without opening a browser
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    ua = UserAgent()
    options.add_argument(f"user-agent={ua.random}")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def scroll_to_load_all_items(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Allow time for page load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def scrape_ebay_items(driver, url):
    driver.get(url)
    time.sleep(5)
    scroll_to_load_all_items(driver)

    scraped_items = []
    try:
        product_elements = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".dne-itemtile"))
        )
    except:
        print("Error: Could not locate product items.")
        product_elements = []

    for product in product_elements:
        try:
            title = product.find_element(By.XPATH, './/span[@itemprop="name"]').text
        except:
            title = "N/A"

        try:
            price = product.find_element(By.XPATH, './/span[@itemprop="price"]').text
        except:
            price = "N/A"

        try:
            original_price = product.find_element(By.XPATH,
                                                  ".//span[contains(@class,'itemtile-price-strikethrough')]").text
        except:
            original_price = price  # If no original price, keep current price

        try:
            item_url = product.find_element(By.XPATH, ".//a[@itemprop='url']").get_attribute("href")
        except:
            item_url = "N/A"

        try:
            shipping_info = product.find_element(By.XPATH, ".//span[contains(@class,'dne-itemtile-delivery')]").text
        except:
            shipping_info = "N/A"

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        item_data = {
            "timestamp": timestamp,
            "title": title,
            "price": price,
            "original_price": original_price,
            "shipping": shipping_info,
            "item_url": item_url,
        }
        scraped_items.append(item_data)

    return scraped_items


def save_data_to_csv(data, filename="ebay_tech_deals.csv"):
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["timestamp", "title", "price", "original_price", "shipping", "item_url"])

    new_entries = pd.DataFrame(data)
    df = pd.concat([df, new_entries], ignore_index=True)
    df.to_csv(filename, index=False)




if __name__ == "__main__":
    EBAY_URL = "https://www.ebay.com/globaldeals/tech"
    driver = setup_driver()
    print("Scraping eBay Items...")
    scraped_items = scrape_ebay_items(driver, EBAY_URL)

    if scraped_items:
        save_data_to_csv(scraped_items)
        print("Data saved to ebay_tech_deals.csv")
    else:
        print("No data found.")

    driver.quit()
