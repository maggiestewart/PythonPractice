from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# define url 
url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/register"

# instantiate webdriver and open chrome browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# maximize browser window
driver.maximize_window()

# load webpage
driver.get(url)

# find first name field
first_name = driver.find_element(By.XPATH, '//*[@id="input-firstname"]')
# fill out first name field
first_name.send_keys("Test")

# find last name field
last_name = driver.find_element(By.XPATH, '//*[@id="input-lastname"]')
# fill out last name field
last_name.send_keys("Testy")

# find email field
email = driver.find_element(By.XPATH, '//*[@id="input-email"]')
# fill out email field
email.send_keys("ttesty@gmail.com")

# find telephone field
telephone = driver.find_element(By.XPATH, '//*[@id="input-telephone"]')
# fill out telephone field
telephone.send_keys("123-456-7890")

# find password field
password = driver.find_element(By.XPATH, '//*[@id="input-password"]')
# fill out password field
password.send_keys("testing!!")

# find password confirmation field
password_confirm = driver.find_element(By.XPATH, '//*[@id="input-confirm"]')
# fill out password confirmation field
password_confirm.send_keys("testing!!")

# find newsletter subscribe field
newsletter_subscribe = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div/div/form/fieldset[3]/div/div/div[2]/label')
# fill out newsletter subscribe field
newsletter_subscribe.click()

# find checkbox to agree with terms
agree = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div/div/form/div/div/div/label')
# check agree 
agree.click()

# find continue button
continue_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div/div/form/div/div/input')
# click continue button
continue_button.click()

# scroll down by 200 units to view lower part of page
driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

# pause program for 5 seconds to view results
sleep(5)

# close driver
driver.quit()