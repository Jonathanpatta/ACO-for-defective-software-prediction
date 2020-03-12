import pandas as pd
import numpy as np






dataset = pd.read_excel("CM1.xls")

dataset['Defective'] = dataset['Defective'].replace("Y",1).replace("N",0)

cols = np.array(dataset.columns)
