# Importing necessary libraries
from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt

# Instantiate a Lasso regressor with an alpha of 0.3
lasso = Lasso(alpha=0.3)

# Fit the model to the data
lasso.fit(X_train, y_train)  # Assuming X_train and y_train are your training data

# Compute the model's coefficients
lasso_coef = lasso.coef_

# Printing the coefficients
print(lasso_coef)

# Plotting the coefficients
plt.bar(sales_columns, lasso_coef)
plt.xticks(rotation=45)
plt.show()
