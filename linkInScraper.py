import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

url = "https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0"
driver = webdriver.Chrome('/Applications/chromedriver_mac64/chromedriver')
driver.get(url)

# Scroll down to load more job postings
scroll_pause_time = 2
scroll_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == scroll_height:
        break
    scroll_height = new_height

# Extract job links and titles
job_lists = driver.find_element(By.CLASS_NAME, "jobs-search__results-list")
jobs = job_lists.find_elements(By.TAG_NAME, "li") # return a list

job_id= []
job_title = []
company_name = []
location = []
date = []
job_link = []

for job in jobs:
    job_id0 = job.get_attribute("data-id")
    job_id.append(job_id0)
    
    job_title0 = job.find_element(By.CSS_SELECTOR, "h3").get_attribute("innerText")
    job_title.append(job_title0)
    
    company_name0 = job.find_element(By.CSS_SELECTOR, "h4").get_attribute("innerText")
    company_name.append(company_name0)
    
    date0 = job.find_element(By.CSS_SELECTOR, "div>div>time").get_attribute("datetime")
    date.append(date0)
    
    job_link0 = job.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
    job_link.append(job_link0)

# Store job details in a dictionary
job_dict = {"Job Title": job_title,
            "Company Name": company_name,
            "Date": date,
            "Job Link": job_link}

# Create a DataFrame from the job details dictionary
df = pd.DataFrame(job_dict)

# Save the DataFrame as a CSV file
df.to_csv("job_details.csv", index=False)

# Close the webdriver
driver.quit()

