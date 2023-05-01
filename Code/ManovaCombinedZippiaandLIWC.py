import pandas as pd
from dfply import *
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.multivariate.manova import MANOVA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as lda


employeedata = pd.read_csv("EmployeeZippiaandLIWC.csv")
executivedata = pd.read_csv("ExecutiveZippiaandLIWC.csv")

employeedata.head(2)
executivedata.head(2)


employeefit = MANOVA.from_formula('Female_Employee_Percentage + Male_Employee_Percentage + \
                                    Female_LIWC + Male_LIWC ~ Industry', data=employeedata)
print("Employee Zippia + LIWC Manova\n", employeefit.mv_test())

executivefit = MANOVA.from_formula('Female_Executive_Percentage + Male_Executive_Percentage + \
                                    Female_LIWC + Male_LIWC ~ Industry', data=executivedata)
print("Executive Zippia + LIWC Manova\n", executivefit.mv_test())




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
