import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation


# load dataset
dataset_col = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8' , 'A9','A10', 'A11', 'A12', 'A13', 'A14' , 'A15', 'A16']
dataset = pd.read_csv("data/cpcrx.data", names=dataset_col)


dataset.head()
print(dataset.describe())

#for replace missing value with NaN
dataset = dataset.replace('?',np.nan)

#function to fill missing value
def fix_missing_mean(dataset,col):
    #replace missing values with mean 
    dataset[col] = pd.to_numeric(dataset[col], errors = 'coerce')
    dataset[col].fillna(dataset[col].mean(), inplace = True)    

def fix_missing_ffill(dataset, col):
    dataset[col] = dataset[col].fillna(method='ffill')  

#fill missing value by column
fix_missing_ffill(dataset,'A1')
fix_missing_ffill(dataset,'A2')
fix_missing_ffill(dataset,'A4')
fix_missing_ffill(dataset,'A5')
fix_missing_ffill(dataset,'A6')
fix_missing_ffill(dataset,'A7')
fix_missing_mean(dataset,'A14')

#checking, is missing va;ue still available
for i in dataset.columns:
    #print(i)
    if dataset[i].dtype==object:
        print(dataset[i].unique())


#mapping character to number by col
d = {'b': 0, 'a': 1}
dataset['A1'] = dataset['A1'].map(d)
d = {'u': 0, 'y': 1, 'l':2, 'g':3}
dataset['A4'] = dataset['A4'].map(d)
d = {'g': 0, 'p': 1, 'gg':2}
dataset['A5'] = dataset['A5'].map(d)
d = {'c':0, 'd':1, 'cc':2, 'i':3, 'j':4, 'k':5, 'm':6, 'r':7, 'q':8, 'w':9, 'x':10, 'e':11, 'aa':12, 'ff':13}
dataset['A6'] = dataset['A6'].map(d)
d = {'v':0, 'h':1, 'bb':2, 'j':3, 'n':4, 'z':5, 'dd':6, 'ff':7, 'o':8}
dataset['A7'] = dataset['A7'].map(d)
d = {'f': 0, 't': 1}
dataset['A9'] = dataset['A9'].map(d)
d = {'f': 0, 't': 1}
dataset['A10'] = dataset['A10'].map(d)
d = {'f': 0, 't': 1}
dataset['A12'] = dataset['A12'].map(d)
d = {'g': 0, 'p': 1, 's':2}
dataset['A13'] = dataset['A13'].map(d)
d = {'+': 1, '-': 0}
dataset['A16'] = dataset['A16'].map(d)

print(dataset)

#Create decition tree
features = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8' , 'A9','A10', 'A11', 'A12', 'A13', 'A14' , 'A15']
X = dataset[features]
y = dataset['A16']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

tree.plot_tree(dtree, feature_names=features)


# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 80% training and 30% test
# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


plt.show()