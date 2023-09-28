import numpy as np
import pandas as pd
import math as math

x_values = np.linspace(0, 2 * math.pi, 1000)
sin_values = np.sin(x_values)

df = pd.DataFrame({'x': x_values, 'sin(x)': sin_values})

df.to_csv('./sin_vs_x_table.csv', index=False)

df.head()