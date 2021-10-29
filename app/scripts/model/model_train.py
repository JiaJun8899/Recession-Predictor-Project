#this program makes use of the datasets created by create_dataset to train and test machine learning models
#K Nearest Neighbors, Support Vector Machine and Linear Regression are the models being tested

import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
import pandas as pd

#specify path where datasets are stored
# Get the directory where this script is running
script_dir = os.path.dirname(__file__)

# Get the generated datasets directory
generated_datasets_dir = os.path.join(script_dir, '../generated_datasets/')

pulled_data_dir = os.path.join(generated_datasets_dir, 'pulled_data/')
clean_data_dir = os.path.join(generated_datasets_dir, 'clean_data/')
processed_data_dir = os.path.join(generated_datasets_dir, 'processed_data/')
misc_graphs_dir = os.path.join(generated_datasets_dir, 'misc_graphs/')
static_dir = os.path.join(script_dir, '../static/')

#import monthly difference dataset
monthly_diff = pd.read_csv(processed_data_dir + 'monthly_diff.csv')
clean_rec_data = pd.read_csv(clean_data_dir + 'clean_rec_data.csv')

#create array of observations and features to be used in training the model
X = monthly_diff[["CPI", "Unemployment Rate", "Market Yield", "Industrial Production Rate", "Treasury Bill Rate", "Capacity Utilization"]]
y = clean_rec_data["Recession"][1:]

#Using k-fold cross validation to determine best K value for KNN model
def knn_param_selection(X, y, nfolds):
    k_range = range(1,31)
    weight = ['uniform', 'distance']
    knn = KNeighborsClassifier()
    knn_param_grid = dict(n_neighbors = k_range, weights = weight)
    knn_grid = GridSearchCV(knn, knn_param_grid, cv = nfolds, scoring = 'accuracy')
    knn_grid.fit(X, y)
    return knn_grid.best_params_, knn_grid.best_score_

#Using k-fold cross validation to determine best parameters for SVM model
def svm_param_selection(X, y, nfolds):
    c_values = [0.001, 0.01, 0.1, 1, 10]
    gamma_values = [0.001, 0.01, 0.1, 1, 10]
    svm_param_grid = {'C': c_values, 'gamma' : gamma_values}
    svm_grid = GridSearchCV(svm.SVC(kernel='rbf'), svm_param_grid, cv=nfolds, scoring = 'accuracy')
    svm_grid.fit(X, y)
    return svm_grid.best_params_, svm_grid.best_score_


#using k-fold cross validation to determine best parameters for logistic regression
def logreg_param_selection(X, y, nfolds):
    logreg = LogisticRegression(max_iter = 1500)
    solvers = ['newton-cg', 'liblinear', 'lbfgs']
    c_values = [0.01, 0.1, 1, 10, 100]
    logreg_param_grid = {'solver': solvers, 'C': c_values}
    logreg_grid = GridSearchCV(logreg, logreg_param_grid, cv = nfolds, scoring = 'accuracy')
    logreg_grid.fit(X, y)
    return logreg_grid.best_params_, logreg_grid.best_score_

knn_results = knn_param_selection(X, y, 10)
svm_results = svm_param_selection(X, y, 10)
logreg_results = logreg_param_selection(X, y, 10)

results = {'KNN': knn_results[1], 'SVM':svm_results[1], 'Logistic Regression': logreg_results[1]}
best_params = {'KNN': knn_results[0], 'SVM':svm_results[0], 'Logistic Regression': logreg_results[0]}

models = list(results.keys())
scores = list(results.values())

#generate bar chart to compare the cross validation scores of the three models
plt.bar(models, scores, width = 0.4)
plt.ylim([0.9, 0.92])
plt.xlabel("Models tested")
plt.ylabel("Best cross validation score")
plt.savefig(static_dir + 'xvalidation.png')
plt.savefig(misc_graphs_dir + 'xvalidation.png')
plt.close()

recent_monthly_diff = pd.read_csv(processed_data_dir + 'recent_merged_data.csv')
recent_X = recent_monthly_diff[
    ["CPI", "Unemployment Rate", "Market Yield", "Industrial Production Rate", "Treasury Bill Rate",
     "Capacity Utilization"]]
maxindex = scores.index(max(scores))
# print(maxindex)
# print(list(best_params[models[maxindex]].values()))
params = list(best_params[models[maxindex]].values())

prediction = 0

if maxindex == 0:
    knn = KNeighborsClassifier(n_neighbors=int(params[0]), weights=(params[1]))
    knn.fit(X, y)
    prediction = int(knn.predict(recent_X))
elif maxindex == 1:
    svm_run = svm.SVC(kernel='rbf', C=float(params[0]), gamma=float(params[1]))
    svm_run.fit(X, y)
    prediction = int(svm_run.predict(recent_X))
elif maxindex == 2:
    logreg = LogisticRegression(max_iter=1500, solver=str(params[1]), C=float(params[0]))
    logreg.fit(X, y)
    prediction = int(logreg.predict(recent_X))

if prediction == 0:
    file1 = open('results.txt', 'w')
    file1.write('According to the {} model trained using historical data from the past 50 years, there will not be a recession this upcoming month.'.format(models[maxindex]))
    file1.close()
elif prediction == 1:
    file1 = open('results.txt', 'w')
    file1.write('According to the {} model trained using historical data from the past 50 years, there will be a recession this upcoming month.'.format(models[maxindex]))
    file1.close()
