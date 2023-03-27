import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


driver = webdriver.Chrome('/Applications/chromedriver_mac64/chromedriver') 

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
    job_descriptions.append(description)
    
    try:
        seniority_level0 = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/section[1]/div/ul/li[1]/span').get_attribute("innerText")
    except:
        seniority_level0 = ""
    seniority_levels.append(seniority_level0)
    
    try:
        industry0 = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/section[1]/div/ul/li[4]/span').get_attribute("innerText")
    except:
        industry0 = ""
    industries.append(industry0)

    try:
        job_function0 = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/section[1]/div/ul/li[3]/span').get_attribute("innerText")
    except:
        job_function0 = ""
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
#job_details.insert(4, column="Job Description", value = job_details)



