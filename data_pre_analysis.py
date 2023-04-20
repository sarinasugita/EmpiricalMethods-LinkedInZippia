import numpy as np
import matplotlib.pyplot as plt
from pandas import *
import os
from scipy import stats

path = 'LIWC_Clean_Results/Industry'

max = 0
max_in = 'None'
files = os.listdir(path)
female_means = []
female_stds = []
male_means = []
male_stds = []
file_names = []
full_female = []
full_male = []
for f in files:
    if f == 'Government_Cleaned.csv':
        continue
    if f == '.DS_Store':
        continue
   # f = 'Government_Cleaned.csv'
    full_name = path + '/' + f
    #print(f)
    data = read_csv(full_name)
    female = data['female'].tolist()
    #print(female)
    female = np.array(female)
    #print(female)
   # print(np.shape(female))
    #print(np.shape(full_female))
    female = female[~np.isnan(female)]
    max_temp = np.max(female)
    if max_temp > max:
        max = max_temp
        max_industry = f
    full_female = np.concatenate([full_female, female])

    male = data['male'].tolist()
    male = np.array(male)
    male = male[~np.isnan(male)]
    max_temp = np.max(male)
   # if max_temp > max:
       # max = max_temp
        #max_industry = f
    full_male = np.concatenate([full_male, male])
    #full_male = full_male + male

    female_mean = np.mean(female)
    male_mean = np.mean(male)

    female_std = np.std(female)
    female_std = np.std(female, ddof=1) / np.sqrt(np.size(female))
    male_std = np.std(male)
    male_std = np.std(male, ddof=1) / np.sqrt(np.size(male))

    file_names.append(f.split('.')[0])
    female_means.append(female_mean)
    male_means.append(male_mean)
    female_stds.append(female_std)
    male_stds.append(male_std)

    print(stats.ttest_rel(male, female), f)

print(max)
print(max_industry)

print(sorted(full_female))



#male_means = np.mean(full_male)
#print(len(full_male))
#print(full_male)
#print(len(full_female))
#female_means = np.mean(full_female)
#male_stds = np.std(full_male)
#male_stds = np.std(full_male, ddof=1) / np.sqrt(np.size(full_male))
#female_stds = np.std(full_female)
ind = np.arange(len(file_names))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, male_means, width, yerr=male_stds,
                label='Male', color='tab:blue')
rects2 = ax.bar(ind + width/2, female_means, width, yerr=female_stds,
                label='Female', color='tab:pink')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Average LIWC Scores (Percentage of Total Words in Job Posting)')
ax.set_xlabel('Seniority Level')
ax.set_title('Average Male and Female LIWC Scores by Seniority Level Job Postings (From LinkedIn)')
ax.set_xticks(ind)
ax.set_xticklabels((file_names))
ax.legend()


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')


#autolabel(rects1, "left")
#autolabel(rects2, "right")

fig.tight_layout()

plt.show()



