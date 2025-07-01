# import relevant libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# define url
url = "http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"

# instantiate webdriver and open chrome browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# maximize browser window
driver.maximize_window()

#load webpage
driver.get(url)

# find source
source = driver.find_element(By.XPATH, '//*[@id="box3"]')

# find destination
destination = driver.find_element(By.XPATH, '//*[@id="box103"]')

# instantiate ActionChains
actions = ActionChains(driver)

# perform drag and drop
actions.drag_and_drop(source, destination).perform()

# pause program for 5 seconds to view results
sleep(5)

# close browser window
driver.quit()
