# Polynomial Regression

# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the Dataset
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


# splitting the dataset into Training Set and Test Set
"""from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)"""

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)"""

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x, y)

# Analysing the result with the simple linear regression
"""from statsmodels.formula.api import OLS
regressor_1 = OLS(endog = y, exog = x).fit()
regressor_1.summary()"""

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
x_poly = poly_reg.fit_transform(x)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)

# Analysing the result with the polynomial regression
"""regressor_2 = OLS(endog = y, exog = x_poly).fit()
regressor_2.summary()"""

# Visualising the Simple linear regression result
plt.scatter(x, y, color='red')
plt.plot(x, lin_reg.predict(x), color='blue')
plt.title('Truth OR Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# Used for higher resolution and smoother curve
"""x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape(len(x_grid),1)"""

# Visualising the Polynomial regression result
plt.scatter(x, y, color='red')
plt.plot(x, lin_reg_2.predict(poly_reg.fit_transform(x)), color='blue') #Change x by x_grid if using 
plt.title('Truth OR Bluff (Ploynomial Regression)')                   #higher resolution and smoother curve
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# Converting the float value to a matrix using numpy
i = 6.5
i = np.array(i).reshape(-1,1)

# Predicting a new result with Linear Regression
lin_reg.predict(i)

# Predicting a new result with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform(i))