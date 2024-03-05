import pandas as pd
#read the excel file 
file = 'ProfitFile.csv'

df = pd.read_csv(file, delimiter=',', decimal='.')
#changes from string to integers
df['Cost'] = pd.to_numeric(df['Cost'], errors='coerce')
df['Current price'] = pd.to_numeric(df['Current price'], errors='coerce')

#excludes promo units
df = df[(df['Cost'] >= 1.01) & (df['Current price'] >= 1.01)]

#Calc profit
df['Profit Margin (%)'] = ((df['Current price'] - df['Cost']) / df['Current price']) * 100
df['Profit Margin (%)'] = df['Profit Margin (%)'].round(2) 
df['Profit Margin (%)'] = df['Profit Margin (%)'].apply(lambda x: f"{x}%")

#sorts by margin
sorted_df = df.sort_values(by='Profit Margin (%)', ascending=False)


sorted_file_path = 'Profit.xlsx'

sorted_df.to_excel(sorted_file_path, index=False)