import requests
from bs4 import BeautifulSoup
import csv
import time


def companyNameExtractor(url):
    """ Ari: Zippia has implemented a strategy of using custom company names in the generation of website links to prevent data scrapers from accessing their data.
    To circumvent this strategy, I created a data scraper that extracts the list of links for the top 100 companies in the finance industry,
    which allows users to access the demographic interface for each company. If you want to use this scraper for industries other than finance,
    such as education, manufacturing, media, etc., you will need to modify the code to extract links for those industries.
    Additionally, you may need to develop your own filtering methods to select the specific companies you are interested in.
    """
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    nameList = set()
    card = soup.find("div", class_="company-centered companyLocationSectionCompanySearchContainer")
    if card:
        for link in card.find_all("a"):
            href = link.get("href")
            if href:
                compName = href.split("/")
                if len(compName) > 2:
                    nameList.add(compName[1])
    return nameList

def demographicExtractor(compName):
    """ Ari: This function allows you to extract gender demographic for the given list of companies.
    I included three attributes: industry type, percentage of employees who are women, and percentage of executives who are women.
    You need to modify the code to fit with your concern. Hope it helps.
    """
    url = "https://www.zippia.com/" + compName + "/demographics/"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    demographicInfo = {}
    tables = soup.find_all("table")
    for table in tables:
        rows = table.find_all("tr")
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 2:
                key = cols[0].text.strip()
                if key in ['Industry', 'Employees Who Are Women', 'Executives Who Are Women']:
                    value = cols[1].text.strip()
                    demographicInfo[key] = value
    return demographicInfo


def saveAll(compNameList, writingmode, headingBool, fileName):
    """ Ari: Save gender demographic information into a csv file called demographics.csv. See demographics.csv for more details, which is generated by this function.

        Note that I only run 50 companies at the same time. This is because Zippia website implements robotics test to prevent access from data scraper.
        To bypass the robotic test, I used "waiting time" stragegy, and only scraped for 50 companies at each time.
    """
    with open(fileName, mode= writingmode, newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if(headingBool): writer.writerow(["Company", "Industry Sub-Group", "Employees Who Are Women", "Executives Who Are Women"])
        for comp in compNameList:
            demographics = demographicExtractor(comp)
            time.sleep(1.5)
            writer.writerow([comp, demographics.get("Industry", ""), demographics.get("Employees Who Are Women", ""),
                             demographics.get("Executives Who Are Women", "")])


compList = companyNameExtractor("https://www.zippia.com/company/government/")

Top50 = list(compList)[:50]
Next50 = list(compList)[50:100]
saveAll(Top50, "w", True, "government100.csv")
time.sleep(10)
saveAll(Next50, "a", False, "government100.csv")

'''
with open("companynames.csv", mode="w", newline = "", encoding= "utf-8") as fi:
    writer = csv.writer(fi)
    for comp in compList:
        writer.writerow([comp])
'''

# print(compNameList)
# print(demographicExtractor("charles-schwab-careers-11417"))