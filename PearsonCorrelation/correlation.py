import numpy as np
import matplotlib.pyplot as plt
from pandas import *
import os
from scipy.stats import pearsonr
import statistics


dict_industries = {}

path = 'LIWC_Clean_Results/Industry'

files = os.listdir(path)
female_means = []
female_stds = []
male_means = []
male_stds = []
file_names = []

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

    female_mean = np.mean(female)
    male_mean = np.mean(male)

    female_std = np.std(female)
    female_std = np.std(female, ddof=1) / np.sqrt(np.size(female))
    male_std = np.std(male)
    male_std = np.std(male, ddof=1) / np.sqrt(np.size(male))

    file_name = f.split('.')[0]
    female_means.append(female_mean)
    male_means.append(male_mean)
    female_stds.append(female_std)
    male_stds.append(male_std)

    dict_industries[file_name] = [(female_mean, female_std, male_mean, male_std)]



path = 'ZippiaTop100Data/Industry'

files = os.listdir(path)
female_means_zip = []
female_stds_zip = []
male_means_zip = []
male_stds_zip = []
file_names_zip = []

for f in files:
    if f == '.DS_Store':
        continue
    full_name = path + '/' + f
    data = read_csv(full_name)
    female = data['Employees Who Are Women'].tolist()
    female = [i.strip('%') for i in female]
    c = female.count('-')
    for i in range(c):
        female.remove('-')

    female = np.array(np.uint8(female))
    female = female / 100

    male = np.full(shape=np.shape(female), fill_value=1)
    male = male - female

    female_mean = np.mean(female)
    male_mean = np.mean(male)

    female_std = np.std(female)
    female_std = np.std(female, ddof=1) / np.sqrt(np.size(female))
    male_std = np.std(male)
    male_std = np.std(male, ddof=1) / np.sqrt(np.size(male))

    file_name = (f.split('.')[0])
    female_means_zip.append(female_mean)
    male_means_zip.append(male_mean)
    female_stds_zip.append(female_std)
    male_stds_zip.append(male_std)

    dict_industries[file_name] = dict_industries[file_name] + [(female_mean, female_std, male_mean, male_std)]



fig, ax = plt.subplots()

color = ['tab:blue', 'tab:orange', 'tab:green','tab:red', 'tab:purple', 'tab:brown',
              'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']

data1 = []
data2 = []

count = 0
for industry in dict_industries:
   # if industry == 'Finance':
        #continue
    #if industry == 'Technology':
        #continue
   # if industry == 'Healthcare':
       # continue
    #if industry == 'Retail':
        #continue
    current_industry = dict_industries[industry]
    current_women_LIWC = current_industry[0][2] / current_industry[0][0]
    current_women_Zippia =  current_industry[1][2]

    data1.append(current_women_LIWC)
    data2.append(current_women_Zippia)

    ax.scatter(current_women_LIWC, current_women_Zippia, c=color[count], label=industry,
               alpha=0.3, edgecolors='none')

    count += 1

a, b = np.polyfit(data1, data2, 1)

#slope, intercept = statistics.linear_regression(data1, data2, proportional=True)

'''
data1 = data1[:,np.newaxis]
a, _, _, _ = np.linalg.lstsq(data1, data2)
'''
#plt.plot(data1, slope*np.float64(data1), color='steelblue', linestyle='-', linewidth=2)

ax.legend()
ax.grid(True)


corr = pearsonr(data1, data2)

#corr, _ = pearsonr(data1, data2)
print(corr)

plt.show()

#print(sorted(data2))

#quit()


print(data1)
print(data2)
corr = pearsonr(data1, data2)

#corr, _ = pearsonr(data1, data2)
print(corr)
#print('Pearsons correlation: %.3f' % corr)



ind = np.arange(len(dict_industries))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, male_means_zip, width, yerr=male_stds_zip,
                label='Male')
rects2 = ax.bar(ind + width/2, female_means_zip, width, yerr=female_stds_zip,
                label='Female')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels((dict_industries.keys()))
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



