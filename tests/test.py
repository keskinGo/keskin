import pandas as pd
import numpy as np

excel_writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')

df = pd.DataFrame(np.random.randn(4, 2), columns=['a', 'b'])
df.style.format("{:.2%}")
df['c'] = ['a', 'b', 'c', 'd']
df.style.format({'c': str.upper})
print(df)



excel_writer.save()