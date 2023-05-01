import pandas as pd
import scipy.stats as stats

data = pd.read_csv("ZippiaTop100Data/Industry/Transportation.csv")

#male = 1-data.iloc[:,2].values[:]
#male = data.iloc[:,2].sub(1)
female = []
male = []
for val in data.iloc[:,3]:
    if val == '-':
        continue
    val = int(val.strip('%'))
    female.append(val)
    male.append(100-val)
pd.Series(male)
pd.Series(female)

print(stats.ttest_rel(female, male))