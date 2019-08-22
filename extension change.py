import os
import pandas as pd
import numpy as np


thisFile = ('C:/Users/HP/Desktop/change_me/color.xls')
base = os.path.splitext(thisFile)[0]
os.rename(thisFile, base + ".csv")


#df = pd.read_csv('C:/Users/HP/Desktop/change_me/color.csv')
#print(df)