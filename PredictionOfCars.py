#Data Preprocessing

#importing the libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the datasets
dataset = pd.read_csv('Social_Network_Ads.csv')
x = dataset.iloc[:,[2,3]].values
y = dataset.iloc[:,4].values 

#Doing the train_test_split for the Datasets
from sklearn.cross_validation import train_test_split 
x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.25, random_state=0)

#Doing the feature scaling for the features
from sklearn.preprocessing import StandardScaler
SC_X=StandardScaler()
x_train=SC_X.fit_transform(x_train)
x_test=SC_X.transform(x_test)

#fitting the logistic regression to Training sets
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)
classifier.fit(x_train,y_train)

#Prediciting the test results values
y_pred=classifier.predict(x_test)

#Confusion Matrix(Evaluating the Logistic regression model)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

#printing the OUTPUT
total=sum(sum(cm))
right_pred=cm[1,1]+(cm[0,0])
wrong_pred=cm[0,1]+(cm[1,0])
acc=(right_pred/100*100)
print("Accuracy= {} %".format(acc))
print("Total predictions made: ",total)
print("Number of right prediction: ",right_pred)
print("Number of anomalous predicition:",wrong_pred)


#Making a Graph for TrainingSet
from matplotlib.colors import ListedColormap
x_set, y_set=x_train, y_train
X1, X2= np.meshgrid(np.arange(start=x_set[:,0].min()-1,stop=x_set[:,0].max()+1,step=0.01),
                    np.arange(start=x_set[:,1].min()-1,stop=x_set[:,1].max()+1,step=0.01))
plt.contourf(X1,X2, classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),
             alpha=0.75,cmap=ListedColormap(('red','green')))
plt.xlim(X1.min(), X1.max())
plt.xlim(X2.min(), X2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set==j,0], x_set[y_set==j,1],
                c=ListedColormap(('red','green'))(i), label=j)
plt.title('Logistic Regression(Training Set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()
