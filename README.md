# Automated Testing Repository

This repository contains automated test scripts for two different functionalities:

1. Amazon Random Dropdown Selection
2. Gmail Login Functionality

## Amazon Random Dropdown Selection & Gmail Login Functionality

### Overview

1. This automated test script demonstrates how to select a dropdown option randomly using Selenium WebDriver in Python.
2. This automated test script demonstrates how to automate basic "Login" functionality test cases for Gmail using Selenium WebDriver in Python.

### Test Execution

1. Ensure you have Python and Selenium WebDriver installed.

2. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/pradipbudhathoki/Automation_Test.git
   
3. Navigate to 'Automation_Test' directory:

   ```bash
   cd Automation_Test
   

4. Activate the virtual environment for python

   ```bash
   python3 -m venv env
   source env/bin/activate
   
5. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt

7. Configure the function on the main.py
   - For Amazon Random Dropdown Selection, use function : **amazon_homepage(driver, logging)** 
   - For Gmail Login Functionality, use function : **gmail_login(driver, logging)**

   **Note:** Use one function at a time.


6. Run the test script:

   ```bash
   python main.py


