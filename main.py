from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.alert import Alert

driver = webdriver.Edge()
action = ActionChains(driver)

driver.get("https://internshala.com/login/student")

# locating the login fields and filling it 
username_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys("rawatsagarblaster2005@gmail.com")
password_field.send_keys("Singh@123")

# for submitting the login form
login_button = driver.find_element(By.ID, "login_submit")
login_button.click()
time.sleep(10)

search_field = driver.find_element(By.LINK_TEXT, "Internships")
search_field.click()
time.sleep(3)

search_field231 = driver.find_element(By.ID, "filter_ui_heading_mobile")
search_field231.click()
time.sleep(3)

search_results = driver.find_element(By.ID, "keywords_mobile")
search_results.send_keys("Computer Science")
time.sleep(2)

search = driver.find_element(By.ID, "search_mobile")
search.click()
time.sleep(3)

view_det = driver.find_element(By.LINK_TEXT, "View details")
view_det.click()
time.sleep(3)

apply_b = driver.find_element(By.LINK_TEXT, "Apply")
apply_b.click()
time.sleep(3)


file_input = driver.find_element(By.NAME, "Upload")  
file_input.send_keys("Path Name")  

time.sleep(3)

text_area = driver.find_element(By.ID, "text_box763")  
personalized_text = "I am passionate about computer science and want to gain real-world experience in this field. I believe this internship will allow me to apply my academic knowledge and develop valuable skills."
text_area.send_keys(personalized_text)



submit_button = driver.find_element(By.ID, "submit_button_id")  
submit_button.click()

time.sleep(10)

# Close the driver
driver.quit()
