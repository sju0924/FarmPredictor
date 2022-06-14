import pandas as pd
from get_param import get_param 
import os


prev_data= pd.read_csv(os.getcwd()+'/mean_data.csv')
a = get_param(prev_data)
print(a)