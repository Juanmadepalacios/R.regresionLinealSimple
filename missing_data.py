#Plantilla de Procesado

#Como importar las librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importar el data set

dataset = pd.read_csv('Data.csv')
X=dataset.iloc[:, :-1].values
y=dataset.iloc[:, 3].values

#Tratamiento de los NAs
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])