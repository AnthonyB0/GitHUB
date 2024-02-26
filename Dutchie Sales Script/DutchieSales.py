from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime, timedelta
import time  # Import the time module
from login import username, password


def launchBrowser():
   chrome_options = Options()
   chrome_options.add_argument("start-maximized")
   chrome_options.add_experimental_option("detach", True)
   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
   driver.get("https://live.backoffice.dutchie.com/reports/closing-report/registers")
   return driver
def login():
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "input-input_login-email"))).send_keys(username)
    wait.until(EC.element_to_be_clickable((By.ID, "input-input_login-password"))).send_keys(password)
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiButton-root.MuiButton-containedPrimary")))
    login_button.click()
def clickDateButton(driver, day_of_month):
    # Click on the input field first
    input_field_id = "input-input_"  # Double-check this ID
    input_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, input_field_id)))
    input_field.click()

    # Construct the XPath for the button dynamically using day_of_month
    # This example assumes the day_of_month somehow alters the button's XPath, which you will need to adjust
    day_div_xpath = f"//div[contains(@class, 'calendar-day') and text()='{day_of_month}']"
    # Wait for the button to be clickable and then click it
    button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
    button.click()
def get_yesterday_day_of_month():
    yesterday = datetime.now() - timedelta(days=1)
    return str(int(yesterday.strftime('%d')))  # Convert to int and back to str to remove leading zero    
def click_yesterday_date_in_calendar(driver, day_of_month):
    # Adjusted to ensure visibility and increase wait time
    day_div_xpath = f"//div[text()='{day_of_month}']"
    try:
        day_div = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, day_div_xpath)))
        click_element_with_js(driver, day_div)
        time.sleep(1)
        button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Run')]")))
        button.click()
    except TimeoutException:
        print("Element not clickable.")
def click_element_with_js(driver, element):
    driver.execute_script("arguments[0].click();", element)
def click_date_input_field(driver):
    date_input_id = "input-input_"  # Adjust if necessary
    date_input = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, date_input_id)))
    date_input.click()
def extract_monetary_values(driver):
    # Construct the CSS selector based on class names
    css_selector = "[class$='table-cell-right-']"

    
    # Wait for the elements to be present and retrieve all matching elements
    elements = WebDriverWait(driver, 6).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector))
    )
    
    # Initialize an empty list to store the extracted monetary values
    monetary_values = []
    
    # Iterate over the retrieved elements and extract the text
    for element in elements[:2]:
        value_text = element.text
        # Optional: Convert the text to a numerical value (float)
        # This assumes the monetary value is in a format like $25,232.81 or ($7,962.09) indicating negative values
        try:
            # Remove the dollar sign and commas, and handle negative values enclosed in parentheses
            numeric_value = float(value_text.replace('$', '').replace(',', '').replace('(', '-').replace(')', ''))
            monetary_values.append(numeric_value)
        except ValueError:
            print(f"Could not convert '{value_text}' to float.")
    return monetary_values
driver = launchBrowser()
login()
click_date_input_field(driver)
day_of_month = get_yesterday_day_of_month()
click_yesterday_date_in_calendar(driver, day_of_month)
gross = extract_monetary_values(driver)
yesterday_formatted = (datetime.now() - timedelta(days=1)).strftime('%m/%d')
if len(gross) >= 2:
    print(f"{yesterday_formatted} Sales was ${gross[0] + gross[1]}")
    print(gross[0], " ", gross[1])
    print(float((-1*gross[1])/gross[0]))
else:
    print("Not enough data to calculate the sum of sales.")
driver.quit()