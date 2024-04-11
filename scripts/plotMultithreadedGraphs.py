import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os

runs = 30

#Load data
dir_path = os.path.dirname(os.path.realpath(__file__))
df = pd.read_csv(f"{dir_path}/../log/threadedTiming.csv")

#Plot threads
df = df.drop("wordAmount",axis=1)

sns.lineplot(x='threadAmount', y='milliSeconds', data=df, errorbar='ci', err_style='bars', 
             marker='o', legend='auto', label='95% Confidence Interval')

plt.title("Execution time with 10.000.000 words at varying thread amounts\n")
#plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
plt.xlabel("Amount of threads")
plt.ylabel("Execution time in MilliSeconds")
plt.grid()
plt.legend(loc='upper right')

plt.savefig(f"{dir_path}/plots/executionTime.png")
plt.clf()

#Plot speedup
df.insert(len(df.columns),'speedup',1)
df.insert(len(df.columns),'stepSpeedup',1)
for ix in df.index:
    df.iloc[ix, df.columns.get_loc('speedup')] = (df.iloc[ix%(runs+1), df.columns.get_loc('milliSeconds')] / 
                                                  df.iloc[ix, df.columns.get_loc('milliSeconds')])
    if ix > runs:
        df.iloc[ix, df.columns.get_loc('stepSpeedup')] = (df.iloc[ix, df.columns.get_loc('speedup')] - 
                                                          df.iloc[ix-(runs+1), df.columns.get_loc('speedup')])

sns.lineplot(x='threadAmount', y='speedup', data=df, errorbar='ci', err_style='bars', 
             marker='o', legend='auto', label='95% Confidence Interval')

plt.title("General speedup with 10.000.000 words at varying thread amounts\n")
#plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
plt.xlabel("Amount of threads")
plt.ylabel("Speedup")
plt.grid()
plt.legend(loc='upper right')
plt.savefig(f"{dir_path}/plots/generalSpeedup.png")
plt.clf()

sns.lineplot(x='threadAmount', y='stepSpeedup', data=df, errorbar='ci', err_style='bars', 
             marker='o', legend='auto', label='95% Confidence Interval')

plt.title("Step speedup with 10.000.000 words at varying thread amounts\n")
#plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
plt.xlabel("Amount of threads")
plt.ylabel("Step speedup")
plt.grid()
plt.legend(loc='upper right')
plt.savefig(f"{dir_path}/plots/stepSpeedup.png")
plt.clf()