#Plantilla de Procesado

#Como importar las librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importar el data set

dataset = pd.read_csv('Data.csv')
X=dataset.iloc[:, :-1].values
y=dataset.iloc[:, 3].values

#Codificar datos categoricos
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:,0])
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)