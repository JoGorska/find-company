import pandas as pd


read_file = pd.read_csv (r'companies.csv')
read_file.to_excel (r'companies.xlsx', index = None, header=True)