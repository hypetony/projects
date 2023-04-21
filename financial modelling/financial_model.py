import pandas as pd

# Define variables
initial_investment = 1000
annual_growth_rate = 0.05
years = 10

# Create dataframe with year and value columns
df = pd.DataFrame({'Year': range(1, years + 1)})
df['Value'] = initial_investment * (1 + annual_growth_rate) ** df['Year']

# Print final value
final_value = df['Value'].iloc[-1]
print(f'The final value after {years} years is ${final_value:.2f}')

