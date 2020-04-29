from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver,600)
target = '"pranjal sharma"'#enter your contact/friend name here
string= "Python Ala re baba PYthon!"#The message you need to send to the contact in whatsapp
#to locate element under span tab
x_arg='//span[contains(@title,'+ target +')]'
target=wait.until(EC.presence_of_element_loctaed((By.XPATH,x_arg)))
target.click()#opens the mesage window of paticular contact selected

 #here find elemeent by class is used to use message box
message_box=driver.find_element_by_class_name('_1Plpp')
for i in range(100):
    message_box.send_keys(string+Keys.ENTER)
