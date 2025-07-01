# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# initial steps
url = "https://the-internet.herokuapp.com/dynamic_controls"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get(url)

# define wait - waits 10 seconds
wait = WebDriverWait(driver, 10)

enable_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/form[2]/button')
enable_button.click()
sleep(3)

disable_button = wait.until(EC.element_to_be_clickable((driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/form[2]/button'))))
disable_button.click()
sleep(3)

remove_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/form[1]/button')
remove_button.click()
sleep(3)

add_button = wait.until(EC.element_to_be_clickable((driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/form[1]/button'))))
add_button.click()
sleep(3)

checkbox = wait.until(EC.element_to_be_clickable((driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/form[1]/div[1]'))))
checkbox.click()
sleep(3)

driver.quit()

