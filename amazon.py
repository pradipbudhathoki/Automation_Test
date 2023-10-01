import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# BASE URL setup
BASE_URL = "https://www.amazon.com/"


def amazon_homepage(driver, logging):
    try:
        logging.info("Connecting Selenium to the AMAZON BASE URL")

        # Setting implicit wait time, script load time & page load time
        driver.implicitly_wait(10)
        driver.set_script_timeout(2)
        driver.set_page_load_timeout(10)

        # Navigate to the amazon homepage
        driver.get(BASE_URL)
        driver.maximize_window()
        logging.info("Selenium Connected AMAZON BASE URL")

        # Search the dropdown menu
        select = Select(driver.find_element(By.ID, "searchDropdownBox"))
        dropdown_options = select.options
        logging.info("Getting values from the dropdown list")
        # Get the dropdown menu attributes and inserts value into an array
        options_name = [name.text for name in dropdown_options]
        # print(options_name)
        # print(len(options_name))

        # Get random value from the dropdown
        logging.info("Selecting random value from the dropdown menu")
        dropdown_index = random.randint(0, len(options_name) - 1)
        select.select_by_index(dropdown_index)
        print("------------ selected dropdown menu {name} -------------".format(name=options_name[dropdown_index]))

        # Click on the search icon to navigate to the corresponding page
        logging.info("Clicking on the search icon")
        search_box = driver.find_element(By.ID, "nav-search-submit-button")
        search_box.click()

        # Sleep time setup to see the webpage
        time.sleep(2)
        logging.info("TEST PASSED")
    except Exception as e:
        logging.error("TEST FAILED")
        logging.error(e)
        # print(f"Unexpected {e=}, {type(e)=}")
    finally:
        # Quit the selenium driver
        driver.quit()
        logging.info("Amazon Test Execution Completed")
