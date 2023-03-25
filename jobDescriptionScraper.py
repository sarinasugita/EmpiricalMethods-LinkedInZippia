import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


driver = webdriver.Chrome('/Applications/chromedriver_mac64/chromedriver') 

job_details = pd.read_csv('job_details.csv')
job_descriptions = []
print(len(job_details))
exception_count = 1
exception2_count = 1
for i in range(len(job_details)):
    link = job_details.iloc[i, 3]

    driver.get(link)

    try:
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "show-more-less-html__button")))
        button.click()
    except:
        print("exception")
    try:
        description = driver.find_element(By.CLASS_NAME, "description__text").get_attribute("innerText")
    except:
        description = ""
        print("exception2")
    job_descriptions.append(description)
"""
    #click on show more button
    try:
        driver.find_element(By.CLASS_NAME, "show-more-less-html__button").click()
    except:
        print(str(exception_count) + "exception")
        exception_count = exception_count + 1
    
    try:
        description = driver.find_element(By.CLASS_NAME, "description__text").get_attribute("innerText")
    except:
        print(str(exception2_count) + "exception2")
        exception2_count = exception2_count + 1
        description = ""

"""


df = pd.DataFrame(job_descriptions)
df.to_csv("job_descriptions.csv")
driver.quit()
#job_details.insert(4, column="Job Description", value = job_details)



