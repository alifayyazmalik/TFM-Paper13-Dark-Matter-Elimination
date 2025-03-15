import pandas as pd
from scipy.optimize import minimize
from tfm_velocity import tfm_velocity

# Load mock data
data = pd.read_csv('data/ngc3198.csv')

def chi2(params):
    lambda_param, beta = params
    v_pred = tfm_velocity(data['r'].values, lambda_param, beta)
    return np.sum((data['v_obs'] - v_pred)**2 / data['err_v']**2)

# Fit parameters (replace with your best-fit values)
initial_guess = [0.5, 0.1]
result = minimize(chi2, initial_guess)

print(f"TFM χ²: {result.fun:.1f}")
print(f"ΛCDM χ²: 22.3 (from Paper #13)")  # Replace with actual ΛCDM value
