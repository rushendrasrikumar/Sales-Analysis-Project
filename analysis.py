import pandas as pd
sales_data = pd.read_csv('C:/Users/mahen/OneDrive/Desktop/Rushi html/sales_force_project/train.csv')
print(sales_data.head())
sales_by_region = sales_data.groupby('Region')['Sales'].sum()
print(sales_by_region)