import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# BASE URL setup
BASE_URL = "https://mail.google.com/"
# BASE_URL = "https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&emr=1&ifkv=AYZoVhfwvN8_E6oKdFJ5gn_U5uJkXA6xZJGUU-bFviD-nUX_uqwaBZ6kLPK9ZsaDBlQObiOorFhjVQ&ltmpl=default&ltmplcache=2&osid=1&passive=true&rm=false&scc=1&service=mail&ss=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1845134469%3A1696092428654499&theme=glif"
USER_NAME = "testautomation584@gmail.com"
PASSWORD = "WakandaForever:2023"


def gmail_login(driver, logging):
    try:
        logging.info("Connecting Selenium to the GMAIL BASE URL")

        # Setting implicit wait time, script load time & page load time
        driver.implicitly_wait(30)
        driver.set_script_timeout(10)
        driver.set_page_load_timeout(10)

        # Navigate to the gmail homepage
        driver.get(BASE_URL)
        driver.maximize_window()
        logging.info("Selenium Connected GMAIL BASE URL")

        # Input on the Email section
        email_input = driver.find_element(By.ID, "identifierId")
        email_input.send_keys(USER_NAME)
        logging.info("Email Address entered")

        # Click Next button after Email is entered
        driver.find_element(By.ID, "identifierNext").click()

        # Input on the Enter your password section
        password_input = driver.find_element(By.XPATH, "//input[@name = 'Passwd']")
        password_input.send_keys(PASSWORD)
        logging.info("Password entered")

        # Optional step to click on show password radio button
        driver.find_element(By.XPATH, "//input[@type = 'checkbox']").click()

        # Click Next button after password is entered
        driver.find_element(By.ID, "passwordNext").click()

        # Explicit wait to check until the Inbox page is reached
        WebDriverWait(driver, 10).until(EC.title_contains("Inbox"))

        # Sleep time setup to see the webpage
        time.sleep(7)
        logging.info("TEST PASSED")
    except Exception as e:
        logging.error("TEST FAILED")
        logging.error(e)
    finally:
        # Quit the selenium driver
        driver.quit()
        logging.info("GMAIL Test Execution Completed")

