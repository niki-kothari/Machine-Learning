try:
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
    import statsmodels.api as sm
    from sklearn.linear_model import LinearRegression
except Exception as e:
    print('Import error:', e)
    raise

# Load data
df = pd.read_csv('advertising.csv')
X = df['TV']
y = df['Sales']

# Train-test split (match notebook settings)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=100)

# Statsmodels OLS
X_train_sm = sm.add_constant(X_train)
lr = sm.OLS(y_train, X_train_sm).fit()
X_test_sm = sm.add_constant(X_test)
y_pred_sm = lr.predict(X_test_sm)

mse_sm = mean_squared_error(y_test, y_pred_sm)
mae_sm = mean_absolute_error(y_test, y_pred_sm)
rmse_sm = np.sqrt(mse_sm)
r2_sm = r2_score(y_test, y_pred_sm)

print('Statsmodels results:')
print(f'MSE: {mse_sm:.6f}')
print(f'MAE: {mae_sm:.6f}')
print(f'RMSE: {rmse_sm:.6f}')
print(f'R2: {r2_sm:.6f}')

# Sklearn LinearRegression
X_train_lm = X_train.values.reshape(-1,1)
X_test_lm = X_test.values.reshape(-1,1)
lm = LinearRegression().fit(X_train_lm, y_train)
y_pred_lm = lm.predict(X_test_lm)

mse_lm = mean_squared_error(y_test, y_pred_lm)
mae_lm = mean_absolute_error(y_test, y_pred_lm)
rmse_lm = np.sqrt(mse_lm)
r2_lm = r2_score(y_test, y_pred_lm)

print('\nSklearn results:')
print(f'MSE: {mse_lm:.6f}')
print(f'MAE: {mae_lm:.6f}')
print(f'RMSE: {rmse_lm:.6f}')
print(f'R2: {r2_lm:.6f}')

