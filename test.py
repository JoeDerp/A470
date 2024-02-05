import numpy as np
import matplotlib.pyplot as plt

# # Generate random data
# h = np.sqrt(np.random.rand(10000))

# # Calculate unit_price
# unit_price = (70 - 50) * h * np.random.rand(10000) + 55 - (55 - 50) * h

# # Calculate variable_costs
# variable_costs = (65000 - 50000) * h * np.random.rand(10000) + 55200 - (55200 - 50000) * h

# # Calculate fixed_costs
# fixed_costs = (20000 - 10000) * h * np.random.rand(10000) + 14000 - (14000 - 10000) * h

# # Calculate unit_sales
# unit_sales = (3000 - 2000) * h * np.random.rand(10000) + 2440 - (2440 - 2000) * h

# # Calculate earnings
# earnings = unit_price * unit_sales - (variable_costs + fixed_costs)

# # Print the first few elements for demonstration
# print("h:", h[:5])
# print("unit_price:", unit_price[:5])
# print("variable_costs:", variable_costs[:5])
# print("fixed_costs:", fixed_costs[:5])
# print("unit_sales:", unit_sales[:5])
# print("earnings:", earnings[:5])

# plt.hist(earnings,bins=15)
# plt.show()



def monteCarloProfitCalc(unitPrice,unitSales,varCost,fixedCost,N):
    unitPriceHat = np.random.default_rng().triangular(unitPrice[0],unitPrice[1],unitPrice[2],N)
    unitSalesHat = np.random.default_rng().triangular(unitSales[0],unitSales[1],unitSales[2],N)
    varCostHat = np.random.default_rng().triangular(varCost[0],varCost[1],varCost[2],N)
    fixedCostHat = np.random.default_rng().triangular(fixedCost[0],fixedCost[1],fixedCost[2],N)
    earnings = []
    for i in range(N):
        earnings.append(unitPriceHat[i]*unitSalesHat[i] - (varCostHat[i]+fixedCostHat[i]))
    return earnings

unitPrice = (50,55,70)
unitSales = (2000,2440,3000)
varCost = (50000,55200,65000)
fixedCost = (10000,14000,20000)
earnings = monteCarloProfitCalc(unitPrice,unitSales,varCost,fixedCost,1000)
plt.hist(earnings,bins=15)
plt.show()




# Generate random data
# h = np.sqrt(np.random.rand(10000))

# # Calculate unit_price, variable_costs, fixed_costs, and unit_sales
# unit_price = (70 - 50) * h * np.random.rand(10000) + 55 - (55 - 50) * h
# variable_costs = (65000 - 50000) * h * np.random.rand(10000) + 55200 - (55200 - 50000) * h
# fixed_costs = (20000 - 10000) * h * np.random.rand(10000) + 14000 - (14000 - 10000) * h
# unit_sales = (3000 - 2000) * h * np.random.rand(10000) + 2440 - (2440 - 2000) * h

# # Calculate base earnings
# earnings_base = unit_price * unit_sales - (variable_costs + fixed_costs)

# # Perform sensitivity analysis by varying one parameter at a time
# param_names = ['unit_price', 'variable_costs', 'fixed_costs', 'unit_sales']
# param_variations = [np.linspace(0.8, 1.2, 5), np.linspace(0.8, 1.2, 5), np.linspace(0.8, 1.2, 5), np.linspace(0.8, 1.2, 5)]

# # Plot sensitivity analysis results
# plt.figure(figsize=(12, 8))

# for i, param_name in enumerate(param_names):
#     plt.subplot(2, 2, i + 1)
#     sensitivity_results = []

#     for variation in param_variations[i]:
#         if i == 0:
#             unit_price_variation = unit_price * variation
#             earnings_variation = unit_price_variation * unit_sales - (variable_costs + fixed_costs)
#         elif i == 1:
#             variable_costs_variation = variable_costs * variation
#             earnings_variation = unit_price * unit_sales - (variable_costs_variation + fixed_costs)
#         elif i == 2:
#             fixed_costs_variation = fixed_costs * variation
#             earnings_variation = unit_price * unit_sales - (variable_costs + fixed_costs_variation)
#         elif i == 3:
#             unit_sales_variation = unit_sales * variation
#             earnings_variation = unit_price * unit_sales_variation - (variable_costs + fixed_costs)

#         sensitivity_results.append(np.mean(earnings_variation))

#     plt.plot(param_variations[i], sensitivity_results, marker='o')
#     plt.title(f'Sensitivity Analysis for {param_name}')
#     plt.xlabel(f'{param_name} Variation')
#     plt.ylabel('Mean Earnings')

# plt.tight_layout()
# plt.show()
