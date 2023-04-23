import pandas as pd
from dfply import *
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.multivariate.manova import MANOVA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as lda


employeedata = pd.read_csv("ZippiaCombinedEmployee.csv")
executivedata = pd.read_csv("ZippiaCombinedExecutive.csv")

employeedata.head(2)
executivedata.head(2)

employee_female_stats = employeedata >> group_by(X.Industry) >> summarize(n=X['Female_Employee_Percentage'].count(), mean=X['Female_Employee_Percentage'].mean(),
                                                                         std=X['Female_Employee_Percentage'].std())
employee_male_stats = employeedata >> group_by(X.Industry) >> summarize(n=X['Male_Employee_Percentage'].count(), mean=X['Male_Employee_Percentage'].mean(),
                                                                         std=X['Male_Employee_Percentage'].std())

executive_female_stats = executivedata >> group_by(X.Industry) >> summarize(n=X['Female_Executive_Percentage'].count(), mean=X['Female_Executive_Percentage'].mean(),
                                                                         std=X['Female_Executive_Percentage'].std())
executive_male_stats = executivedata >> group_by(X.Industry) >> summarize(n=X['Male_Executive_Percentage'].count(), mean=X['Male_Executive_Percentage'].mean(),
                                                                         std=X['Male_Executive_Percentage'].std())


print("Employee Female Stats\n", employee_female_stats, "\n")
print("Employee Male Stats\n", employee_male_stats, "\n")
print("Executive Female Stats\n", executive_female_stats, "\n")
print("Executive Male Stats\n", executive_male_stats, "\n")


employeefit = MANOVA.from_formula('Female_Employee_Percentage + Male_Employee_Percentage ~ Industry', data=employeedata)
print("Employee Manova\n", employeefit.mv_test())

executivefit = MANOVA.from_formula('Female_Executive_Percentage + Male_Executive_Percentage ~ Industry', data=executivedata)
print("Executive Manova\n", executivefit.mv_test())




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
