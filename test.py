import numpy as np
import matplotlib.pyplot as plt

# Generate random data
h = np.sqrt(np.random.rand(10000))

# Calculate unit_price, variable_costs, fixed_costs, and unit_sales
unit_price = (70 - 50) * h * np.random.rand(10000) + 55 - (55 - 50) * h
variable_costs = (65000 - 50000) * h * np.random.rand(10000) + 55200 - (55200 - 50000) * h
fixed_costs = (20000 - 10000) * h * np.random.rand(10000) + 14000 - (14000 - 10000) * h
unit_sales = (3000 - 2000) * h * np.random.rand(10000) + 2440 - (2440 - 2000) * h

# Calculate base earnings
earnings_base = unit_price * unit_sales - (variable_costs + fixed_costs)

# Perform sensitivity analysis by varying one parameter at a time
param_names = ['unit_price', 'variable_costs', 'fixed_costs', 'unit_sales']
param_variations = [np.linspace(0.8, 1.2, 5), np.linspace(0.8, 1.2, 5), np.linspace(0.8, 1.2, 5), np.linspace(0.8, 1.2, 5)]

# Plot sensitivity analysis results with confidence interval
sensitivity_results = []

plt.figure(figsize=(12, 8))

for i, param_name in enumerate(param_names):
    for variation in param_variations[i]:
        if i == 0:
            unit_price_variation = unit_price * variation
            earnings_variation = unit_price_variation * unit_sales - (variable_costs + fixed_costs)
        elif i == 1:
            variable_costs_variation = variable_costs * variation
            earnings_variation = unit_price * unit_sales - (variable_costs_variation + fixed_costs)
        elif i == 2:
            fixed_costs_variation = fixed_costs * variation
            earnings_variation = unit_price * unit_sales - (variable_costs + fixed_costs_variation)
        elif i == 3:
            unit_sales_variation = unit_sales * variation
            earnings_variation = unit_price * unit_sales_variation - (variable_costs + fixed_costs)

        sensitivity_results.append(np.mean(earnings_variation))

# Calculate confidence interval for the entire simulation
confidence_interval = 1.96 * np.std(sensitivity_results) / np.sqrt(len(sensitivity_results))

# Plot the results
plt.errorbar(np.arange(len(sensitivity_results)), sensitivity_results, yerr=confidence_interval,
             fmt='o', label='Conf. Int.')
plt.title('Sensitivity Analysis for the Entire Simulation')
plt.xlabel('Simulation Samples')
plt.ylabel('Mean Earnings')
plt.legend()
plt.show()
