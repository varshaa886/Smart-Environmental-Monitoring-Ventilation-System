import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error, r2_score

# Load Excel file (change filename accordingly)
file_path = "eg.xlsx"
df = pd.read_excel(file_path, header=None)

# Extract data (assuming first column is X and second is Y)
x_values = df.iloc[:, 0].values
y_actual = df.iloc[:, 1].values

# Apply Savitzky-Golay filter for smoothing
y_smoothed = savgol_filter(y_actual, window_length=1669, polyorder=3)

# Define exponential function for curve fitting
def exp_func(x, a, b, c):
    return a * np.exp(b * x) + c

# Perform curve fitting on smoothed data
popt, pcov = curve_fit(exp_func, x_values, y_smoothed, maxfev=10000)
a_fit, b_fit, c_fit = popt

# Generate fitted curve using optimized parameters
y_fitted = exp_func(x_values, a_fit, b_fit, c_fit)

# Calculate error metrics between fitted curve and smoothed data
SSE = np.sum((y_smoothed - y_fitted) ** 2)
RMSE = np.sqrt(mean_squared_error(y_smoothed, y_fitted))
R2 = r2_score(y_smoothed, y_fitted)

# Print error metrics
print(f"Fitted Equation: y = {a_fit:.2f} * exp({b_fit:.2f} * x) + {c_fit:.2f}")
print(f"SSE: {SSE:.4f}")
print(f"RMSE: {RMSE:.4f}")
print(f"R²: {R2:.4f}")

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_actual, label="Original Data", linestyle="dotted", alpha=1, linewidth=1.5)
plt.plot(x_values, y_smoothed, label="Smoothed Curve",linestyle="dashed", color="red", linewidth=2)
plt.plot(x_values, y_fitted, label=f"Fitted Curve: y = {a_fit:.2f}exp({b_fit:.2f}x) + {c_fit:.2f}",
         color="green",  linewidth=1.5)

# Get current axes
ax = plt.gca()

# Define box properties
props = dict(boxstyle='square', facecolor='white', edgecolor='black', linewidth=1, alpha=0.5)

# Place the R² value in the upper left corner inside the plot
ax.text(0.05, 0.95, f'$R^2 = {R2:.4f}$', transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)

plt.xlabel("Time (Hours)", fontsize=12)
plt.ylabel("CO₂ Concentration (ppm)", fontsize=12)
plt.legend()
plt.grid()
plt.subplots_adjust(top=0.945, bottom=0.105, left=0.09, right=0.975)
plt.show()