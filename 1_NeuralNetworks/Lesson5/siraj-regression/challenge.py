import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

# read data
dataframe = pd.read_csv('challenge_dataset.txt', header=None, sep=',', names=['Brain', 'Body'])
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]

# Training the model
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

# visualize results
plt.scatter(x_values, y_values)
plt.plot(x_values, body_reg.predict(x_values))
plt.show()
