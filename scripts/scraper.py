import time

from selenium import webdriver


print("Sample test started")


def get_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver


def get_page_source(link=None):
    driver = get_browser()
    driver.get(link)
    page_source = driver.page_source
    print(page_source)
    time.sleep(3)
    driver.close()

    return page_source