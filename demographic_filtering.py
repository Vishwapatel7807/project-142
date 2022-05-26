import pandas as pd 
import numpy as np 

df = pd.read_csv('final.csv') 
 
df1 = df1.sort_values(['total_events'], ascending=[False]) 
df1.head()
