import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

data = pd.read_csv('Data_for_UCI_named.csv')
x = data.drop('stabf', axis=1)
y = np.array(pd.get_dummies(data.stabf, drop_first=True)).ravel()
print(y)

train_x, test_x, train_y, test_y = train_test_split(x, y, random_state=101, test_size=0.3)

scaler = StandardScaler()
train_x = scaler.fit_transform(train_x)
test_x = scaler.fit_transform(test_x)

classifier = LogisticRegression()
classifier.fit(train_x, train_y)
predictor = classifier.predict(test_x)

eval = pd.DataFrame({'test':test_y, 'predict':predictor})
print(eval.head(20))
print('Accuracy: ', np.mean(predictor == test_y))
print(classification_report(test_y, predictor))
print(confusion_matrix(test_y, predictor))

