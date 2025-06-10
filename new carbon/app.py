import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000

# Generate synthetic data
diesel_l = np.random.randint(800, 2500, size=n)
electricity_kwh = np.random.randint(5000, 12000, size=n)
paint_l = np.random.randint(100, 350, size=n)
welding_count = np.random.randint(5, 30, size=n)
transport_km = np.random.randint(100, 400, size=n)

# Emissions calculation
emissions = (diesel_l * 2.68 + electricity_kwh * 0.5 + paint_l * 3.5 + welding_count * 1.2 + transport_km * 0.2)

# Root cause determination
root_cause = []
for d, e, p, w, t in zip(diesel_l, electricity_kwh, paint_l, welding_count, transport_km):
    factors = {'Diesel': d * 2.68, 'Electricity': e * 0.5, 'Paint': p * 3.5, 'Welding': w * 1.2, 'Transport': t * 0.2}
    max_cause = max(factors, key=factors.get)
    root_cause.append(max_cause)

cost_before = emissions * 40 + np.random.randint(10000, 20000, size=n)
cost_after = cost_before - np.random.randint(5000, 15000, size=n)

# Create DataFrame
df = pd.DataFrame({
    'Diesel_L': diesel_l,
    'Electricity_kWh': electricity_kwh,
    'Paint_L': paint_l,
    'Welding_Count': welding_count,
    'Transport_km': transport_km,
    'Emissions_kgCO2e': emissions,
    'Root_Cause': root_cause,
    'Cost_Before': cost_before,
    'Cost_After': cost_after,
})

# Add date columns for monthly data starting Jan 2000
date_range = pd.date_range(start='2000-01-01', periods=n, freq='MS')
df['Date'] = date_range
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Save CSV locally
df.to_csv('automotive_emission_dataset_with_date.csv', index=False)

print("CSV file 'automotive_emission_dataset_with_date.csv' has been created successfully.")
