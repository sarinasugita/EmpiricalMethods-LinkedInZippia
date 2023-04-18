import pandas as pd
from dfply import *
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.multivariate.manova import MANOVA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as lda


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    senioritydata = pd.read_csv("ManovaSeniorityData.csv")
    senioritydata.head(2)
    seniority_female_stats = senioritydata >> group_by(X.Level) >> summarize(n=X['Female'].count(), mean=X['Female'].mean(), std=X['Female'].std())
    seniority_male_stats = senioritydata >> group_by(X.Level) >> summarize(n=X['Male'].count(), mean=X['Male'].mean(),
                                                    std=X['Male'].std())

    print("Seniority Female Stats\n", seniority_female_stats)
    print("Seniority Male Stats\n", seniority_male_stats)

    '''
    BOXPLOT -- NOT USED

    # Female boxplot
    fig, ax1 = plt.subplots()
    senioritydata['Female_rescaled'] = senioritydata['Female'] * 100
    sns.boxplot(data=senioritydata, x="Level", y="Female", hue=senioritydata.Level.tolist(), ax=ax1)
    ax1.legend(title='Level', bbox_to_anchor=(1, 1), loc='upper left')
    plt.show()

    # Male boxplot
    fig2, ax2 = plt.subplots()
    sns.boxplot(data=senioritydata, x="Level", y="Male", hue=senioritydata.Level.tolist(), ax=ax2)
    ax2.legend(title='Level', bbox_to_anchor=(1, 1), loc='upper left')
    plt.show()
    
    '''
    fit = MANOVA.from_formula('Female + Male ~ Level', data=senioritydata)
    print(fit.mv_test())

    '''
    CONFUSING LDA SCATTERPLOT
    
    X = senioritydata[["Female", "Male"]]
    y = senioritydata["Level"]
    post_hoc = lda().fit(X=X, y=y)

    #print(post_hoc.means_)    

    X_new = pd.DataFrame(lda().fit(X=X, y=y).transform(X), columns=["lda1", "lda2"])
    X_new["Level"] = senioritydata["Level"]
    sns.scatterplot(data=X_new, x="lda1", y="lda2", hue=senioritydata.Level.tolist())
    plt.show()
    
    '''


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
