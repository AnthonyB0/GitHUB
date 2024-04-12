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
   driver.get("https://ds.calstate.edu/?svc=CS&env=CSDPRD&org=SDSU")
   return driver
def login():
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "i0116"))).send_keys(username)
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
    login_button.click()
    wait.until(EC.element_to_be_clickable((By.ID, "i0118"))).send_keys(password)
    sign_button = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
    sign_button.click()
    duo = wait.until( EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Send Me a Push')]")))
    duo.click()
    time.sleep(7)
    yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Yes']")))
    yes_button.click()
def classes():
    mc_button = WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.ID, "win0groupletPTNUI_LAND_REC_GROUPLET$6")))
    mc_button.click()
    time.sleep(3)
    summer_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "win5divSSR_ENTRMCUR_VW_ACAD_CAREER_DESCR$1")))
    summer_button.click()

    #fall_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "SSR_ENTRMCUR_VW_TERM_DESCR30$2")))
    #fall_button.click()

    shopping_cart_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "SCC_LO_FL_WRK_SCC_VIEW_BTN$2"))
)
    driver.execute_script("arguments[0].click();", shopping_cart_button)

    summer_button2 = WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.ID, "SSR_CART_TRM_FL_TERM_DESCR30$0")))
    summer_button2.click()

    #fall_button2 = WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.ID, "ACAD_CAR_TBL_DESCR$1")))
    #fall_button2.click()

    

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "ps-checkbox"))
    )
    
    # Use the corrected method to find elements by class name
    checkboxes = driver.find_elements(By.CLASS_NAME, "ps-checkbox")
    
    # Iterate over each checkbox and click it if it is not already checked
    for checkbox in checkboxes:
        # Check if the checkbox is visible and not already checked before clicking
        if checkbox.is_displayed() and not checkbox.is_selected():
            # Scroll into view and click the checkbox
            driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
            checkbox.click()
    enroll_button2 = WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.ID, "DERIVED_SSR_FL_SSR_ENROLL_FL")))
    enroll_button2.click()
driver = launchBrowser()
login()
classes()