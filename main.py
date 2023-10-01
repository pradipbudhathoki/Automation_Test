from amazon import amazon_homepage
from mail_login import gmail_login
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import logging

# logging message config setup
logging.basicConfig(level=logging.INFO
                    , format="%(asctime)s %(levelname)s %(message)s"
                    , datefmt="%Y-%m-%d %H:%M:%S")

options = Options()

# setting to load page normally and to make the browser headless
options.page_load_strategy = 'normal'
# options.add_argument("--headless")
driver = Chrome(options=options)

if __name__ == '__main__':
    amazon_homepage(driver, logging)
    # gmail_login(driver, logging)
