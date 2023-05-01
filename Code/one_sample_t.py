import numpy as np
import matplotlib.pyplot as plt
from pandas import *
import os
from scipy.stats import pearsonr
from scipy import stats
import statistics


#LinkendIn
all_industries = 'ManovaSeniority/ManovaSeniorityData.csv'

male_data = np.loadtxt(all_industries, delimiter=',', skiprows=1, usecols=2)
female_data = np.loadtxt(all_industries, delimiter=',', skiprows=1, usecols=1)

male_mean = np.mean(male_data)
female_mean = np.mean(female_data)

male_female_ratio_mean = male_mean /female_mean


path = 'LIWC_Clean_Results/Seniority'

files = os.listdir(path)
female_t = {}
male_t = {}
male_female_t = {}



for f in files:
    if f == '.DS_Store':
        continue
    full_name = path + '/' + f
    data = read_csv(full_name)
    female = data['female'].tolist()
    female = np.array(female)
    female = female[~np.isnan(female)]

    male = data['male'].tolist()
    male = np.array(male)
    male = male[~np.isnan(male)]

    t_statistic, p_value = stats.ttest_1samp(a=female, popmean=female_mean)

    file_name = f.split('.')[0]

    if file_name in female_t:

        female_t[file_name] = female_t[file_name]  + [(t_statistic, p_value)]

    else:

        female_t[file_name] = [(t_statistic, p_value)]

    t_statistic, p_value = stats.ttest_1samp(a=male, popmean=male_mean)

    file_name = f.split('.')[0]

    if file_name in male_t:

        male_t[file_name] = male_t[file_name] + [(t_statistic, p_value)]

    else:

        male_t[file_name] = [(t_statistic, p_value)]


#print(male_mean)
#print(male_t)




#Zippia

path = 'ZippiaTop100Data/Industry'

files = os.listdir(path)

full_female = []
full_male = []

for f in files:
    if f == '.DS_Store':
        continue
    full_name = path + '/' + f
    data = read_csv(full_name)
    female = data['Executives Who Are Women'].tolist()
    female = [i.strip('%') for i in female]
    c = female.count('-')
    for i in range(c):
        female.remove('-')

    female = np.array(np.uint8(female))
    full_female = full_female + list(female)
    #female = female / 100

    male = np.full(shape=np.shape(female), fill_value=100)
    male = male - female
    full_male = full_male + list(male)


male_mean = np.mean(full_male)
female_mean = np.mean(full_female)


female_t = {}
male_t = {}

for f in files:
    if f == '.DS_Store':
        continue
    full_name = path + '/' + f
    data = read_csv(full_name)
    female = data['Executives Who Are Women'].tolist()
    female = [i.strip('%') for i in female]
    c = female.count('-')
    for i in range(c):
        female.remove('-')

    female = np.array(np.uint8(female))

    male = np.full(shape=np.shape(female), fill_value=100)
    male = male - female

    t_statistic, p_value = stats.ttest_1samp(a=female, popmean=female_mean)

    file_name = f.split('.')[0]

    if file_name in female_t:

        female_t[file_name] = female_t[file_name] + [(t_statistic, p_value)]

    else:

        female_t[file_name] = [(t_statistic, p_value)]

    t_statistic, p_value = stats.ttest_1samp(a=male, popmean=male_mean)

    file_name = f.split('.')[0]

    if file_name in male_t:

        male_t[file_name] = male_t[file_name] + [(t_statistic, p_value)]

    else:

        male_t[file_name] = [(t_statistic, p_value)]


print(male_mean)
print(male_t)





