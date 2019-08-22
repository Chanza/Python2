
import pandas as pd
import numpy as np

data = pd.read_excel('C:/Users/HP/Desktop/failed billed zamtel.xlsx')
X = data.iloc[:,2:]  #independent columns
y = data.iloc[:,:1]    #target column i.e price range

#print(X)
#print(y)

from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
model = ExtraTreesClassifier()
model.fit(X,y)
print(model.feature_importances_) #use inbuilt class feature_importances of tree based classifiers
#plot graph of feature importances for better visualization
feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(10).plot(kind='barh')
plt.show()


























