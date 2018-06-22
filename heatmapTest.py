import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc
import numpy as np

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# df = pd.read_csv('c:/seoul_bigdata/category_perStore_02.csv', delimiter=',')
df = pd.read_csv('c:/seoul_bigdata/category_category.csv', delimiter=',')

print(len(df.columns))
print(df.shape)

df = df.iloc[ : , np.r_[18, 32]]
df = df[df.의류점 != 0]
df = df[df.패션잡화 != 0]

print(len(df))

print(df.head(30))

plt.figure(figsize=(15,15))
sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=plt.cm.gist_heat, linecolor='white', annot=True)
plt.show()

