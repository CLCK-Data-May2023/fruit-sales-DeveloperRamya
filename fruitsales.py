import pandas as pd 
fruit-sales = pd.DataFrame({'Apples':[35,41], 'Bananas':[21,34]}, index=['2017 Sales','2018 Sales'])
fruit-sales.to_csv('fruit.csv')
