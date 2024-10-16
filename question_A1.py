import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('Superstore_dataset.csv')

#---------- all regions mean profit get
mean_profit_per_region = data.groupby('Region')['Profit'].mean().reset_index()
print(mean_profit_per_region)

#----------- profit < 27%  regions  identify
regions_to_discontinue = mean_profit_per_region[mean_profit_per_region['Profit'] < 27]['Region'].tolist()
print(regions_to_discontinue)

top_region = data[~data['Region'].isin(regions_to_discontinue)]
print(top_region)

plt.figure(figsize=(10, 6))
plt.bar(mean_profit_per_region['Region'], mean_profit_per_region['Profit'], color='skyblue')
plt.xlabel('Region')
plt.ylabel('Mean Profit')
plt.title('Mean Profit per Region')
plt.axhline(y=27, color='red', linestyle='--', label='Discontinue Threshold (27)')
plt.legend()
plt.show()


print("Regions to be discontinued:", regions_to_discontinue)
print("Top Regions DataFrame shape:", top_region.shape)
print(top_region.head())