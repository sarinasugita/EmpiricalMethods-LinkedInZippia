import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

start=datetime.now()

#Change path to where your downloaded chromedriver is located
s = Service('C:/Users/honganndo/Downloads/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service = s)

job_details = pd.read_csv('job_details.csv')
job_descriptions = []
seniority_levels = []
industries = []
job_functions = []

print(len(job_details))
exception_count = 1
exception2_count = 1
for i in range(len(job_details)):
    link = job_details.iloc[i, 3]
    time.sleep(4)
    driver.get(link)
    print(i)

    try:
        button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "show-more-less-html__button")))
        button.click()
    except:
        time.sleep(5)
        driver.get(link)
        try:
            button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "show-more-less-html__button")))
            button.click()
        except:
            print("exception")
    try:
        job_desc_elem = driver.find_element(By.CLASS_NAME, "show-more-less-html__markup")
        soup = BeautifulSoup(job_desc_elem.get_attribute('outerHTML'), 'html.parser')
        # The parser will get the full description within the show more less html mark up element.
        # Use 'separator = \n' to print each each paragraph on a new line and '\n\n' to print an empty line between paragraphs
        description = soup.get_text(separator='\n\n')
    except:
        description = "n/a"
    job_descriptions.append(description)
    
    try:
        seniority_level0 = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/section[1]/div/ul/li[1]/span').get_attribute("innerText")
    except:
        seniority_level0 = "n/a"
    seniority_levels.append(seniority_level0)
    
    try:
        industry0 = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/section[1]/div/ul/li[4]/span').get_attribute("innerText")
    except:
        industry0 = "n/a"
    industries.append(industry0)

    try:
        job_function0 = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/section[1]/div/ul/li[3]/span').get_attribute("innerText")
    except:
        job_function0 = "n/a"
    job_functions.append(job_function0)

# Store job details in a dictionary
job_dict = {"Job Function": job_functions,
            "Industry": industries,
            "Seniority": seniority_levels,
            "Job Description": job_descriptions}

# Create a DataFrame from the job details dictionary
df = pd.DataFrame(job_dict)

df.to_csv("job_descriptions.csv")
driver.quit()
print (datetime.now()-start)
#job_details.insert(4, column="Job Description", value = job_details)



