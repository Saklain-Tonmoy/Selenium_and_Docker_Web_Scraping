import time

from selenium import webdriver

def get_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--mute-audio')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--ignore-certificate-errors-spki-list')
    chrome_options.add_argument('--no-zygote')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--disable-features=VizDisplayCompositor')
    chrome_options.add_argument('--disable-breakpad')
    # Set desired capabilities to ignore SSL stuffs
    desired_capabilities = chrome_options.to_capabilities()
    desired_capabilities['acceptInsecureCerts'] = True
    driver = webdriver.Chrome(options=chrome_options, desired_capabilities=desired_capabilities)
    driver.maximize_window()
    return driver


def get_page_source(link=None):
    driver = get_browser()
    driver.get(link)
    page_source = driver.page_source
    time.sleep(3)
    driver.close()

    return page_source