import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os
import locale
locale.setlocale(locale.LC_ALL, '')

runs = 20
word_amount_list = [1000,100000,10000000]
#word_amount_list = [1000,100000,10000000,100000000]

#Load data
dir_path = os.path.dirname(os.path.realpath(__file__))
df = pd.read_csv(f"{dir_path}/../log/threadedTiming.csv")

#Adjust to Milliseconds
df['microSeconds'] = df['microSeconds'] / 1000

#Plot threads
for word_amount in word_amount_list:
    if word_amount != word_amount_list[0] and word_amount != word_amount_list[1]:
        continue
    line_df = df.loc[df['wordAmount'] == word_amount]
    sns.lineplot(x='threadAmount', y='microSeconds', data=line_df, errorbar=None, err_style='bars', 
                 marker='o', legend='auto', label=f'{word_amount:n} words')

plt.title("Mean execution time at varying thread amounts\n")
#plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
plt.xlabel("Amount of threads")
plt.ylabel("Execution time in Milliseconds (ms)")
plt.grid()
plt.legend(loc='upper right')

plt.savefig(f"{dir_path}/plots/executionTime1.png")
plt.clf()

#Plot threads
for ix, word_amount in enumerate(word_amount_list):
    if word_amount == word_amount_list[0] or word_amount == word_amount_list[1]:
        continue
    line_df = df.loc[df['wordAmount'] == word_amount]
    sns.lineplot(x='threadAmount', y='microSeconds', data=line_df, errorbar=None,
                 marker='o', legend='auto', label=f'{word_amount:n} words')

    plt.title("Mean execution time at varying thread amounts\n")
    #plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
    plt.xlabel("Amount of threads")
    plt.ylabel("Execution time in Milliseconds (ms)")
    plt.grid()
    plt.legend(loc='upper right')

    plt.savefig(f"{dir_path}/plots/executionTime{ix}.png")
    plt.clf()

#Plot speedup
df.insert(len(df.columns),'speedup',1)

for word_amount in word_amount_list:
    line_df = df.loc[df['wordAmount'] == word_amount]
    line_df = line_df.reset_index(drop=True)
    for ix in line_df.index:
        line_df.iloc[ix, line_df.columns.get_loc('speedup')] = (line_df.iloc[ix%runs, line_df.columns.get_loc('microSeconds')] / 
                                                                line_df.iloc[ix, line_df.columns.get_loc('microSeconds')])
    sns.lineplot(x='threadAmount', y='speedup', data=line_df, errorbar=None,
                 marker='o', legend='auto', label=f'{word_amount:n} words')

plt.title("Cumulative speedup at varying thread amounts\n")
#plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
plt.xlabel("Amount of threads")
plt.ylabel("Speedup")
plt.grid()
plt.legend(loc='upper left')
plt.savefig(f"{dir_path}/plots/cumulativeSpeedup.png")
plt.clf()


##Plot Scalability at 20 Threads
#line_df = df.loc[df['threadAmount'] == 20]
#line_df = line_df.reset_index(drop=True)
#
#sns.lineplot(x='wordAmount', y='microSeconds', data=line_df, errorbar=None,
#             marker='o', legend='auto', label=f'Mean execution time')
#
#plt.title("Scalability at 20 threads\n")
##plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
#plt.xlabel("Amount of words")
#plt.ylabel("Execution time in Microseconds (us)")
#plt.grid()
#plt.legend(loc='upper left')
#plt.savefig(f"{dir_path}/plots/scalability.png")
#plt.clf()

