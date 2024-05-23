import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os
import locale
locale.setlocale(locale.LC_ALL, '')

runs = 20
word_amount_list = [1000,100000,10000000]

#Load data
dir_path = os.path.dirname(os.path.realpath(__file__))
df_unopt = pd.read_csv(f"{dir_path}/../log/threadedTiming-unopt.csv")
df_opt1 = pd.read_csv(f"{dir_path}/../log/threadedTiming-opt1.csv")
df_opt2 = pd.read_csv(f"{dir_path}/../log/threadedTiming-opt2.csv")

#Filter data for 10.000.000 words
df_unopt = df_unopt.loc[df_unopt['wordAmount'] == 10000000]
df_unopt = df_unopt.reset_index(drop=True)
df_unopt['microSeconds'] = df_unopt['microSeconds'] / 1000
df_opt1 = df_opt1.loc[df_opt1['wordAmount'] == 10000000]
df_opt1 = df_opt1.reset_index(drop=True)
df_opt1['microSeconds'] = df_opt1['microSeconds'] / 1000
df_opt2 = df_opt2.loc[df_opt2['wordAmount'] == 10000000]
df_opt2 = df_opt2.reset_index(drop=True)
df_opt2['microSeconds'] = df_opt2['microSeconds'] / 1000

#Plot comparative mean execution time graph
sns.lineplot(x='threadAmount', y='microSeconds', data=df_unopt, errorbar=None,
                 marker='o', legend='auto', label=f'Unoptimized')
sns.lineplot(x='threadAmount', y='microSeconds', data=df_opt1, errorbar=None,
                 marker='o', legend='auto', label=f'MurMur')
sns.lineplot(x='threadAmount', y='microSeconds', data=df_opt2, errorbar=None,
                 marker='o', legend='auto', label=f'MurMur + Pinning')

plt.title("Mean execution time at varying thread amounts for different versions\n")
plt.xlabel("Amount of threads")
plt.ylabel("Execution time in Milliseconds (ms)")
plt.grid()
plt.legend(loc='upper right')

plt.savefig(f"{dir_path}/plots/executionTimeRecap.png")
plt.clf()

