import pandas as pd
import matplotlib.pyplot as plt

# 5.1:
url_total_2008 = "https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=000&CIVILSTAND=F%2CTOT&Tid=2008K4"
url_2020 = "https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=000&CIVILSTAND=F%2CTOT&Tid=%2C2020K4"

df_total_2008 = pd.read_csv(url_total_2008, sep=';')
df_total_2020 = pd.read_csv(url_2020, sep=';')

num_population_2008 = df_total_2008.iloc[1, 3]
num_divorced_2008 = df_total_2008.iloc[0, 3]

num_population_2020 = df_total_2020.iloc[1, 3]
num_divorced_2020 = df_total_2020.iloc[0, 3]

num_pct_2008 = num_divorced_2008 / num_population_2008 * 100
num_pct_2020 = num_divorced_2020 / num_population_2020 * 100

print("Divorced in 2008: ")
print(num_pct_2008)
print("Divorced in 2020: ")
print(num_pct_2020)

dict_divorced = {"2008 : num_pct_2008", "2020 : num_pct_2020"}

'''
keys = dict_divorced.keys()
values = dict_divorced.values()

def show_divorced():
    plt.bar(keys, values, width=0.5, align='center')
    plt.xlabel("Year")
    plt.ylabel("Divorced")
    plt.xticks(rotation=20, horizontalalignment='right', fontweight='light', fontsize='x-small')
    plt.show()


show_divorced()
'''


# 5.2:
url_top5_total = "https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=Value&delimiter=Semicolon&OMR%C3%85DE=101%2C751%2C461%2C851%2C147&Tid=2020K4"
url_top5_unmarried = "https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=Value&delimiter=Semicolon&OMR%C3%85DE=101%2C751%2C461%2C851%2C147&Tid=2020K4&CIVILSTAND=U"

df_top5_total = pd.read_csv(url_top5_total, sep=';')
df_top5_unmarried = pd.read_csv(url_top5_unmarried, sep=';')

df_top5_merged = pd.merge(df_top5_total, df_top5_unmarried, left_on='OMRÅDE', right_on='OMRÅDE')
df_top5_filtered = df_top5_merged[["OMRÅDE", "INDHOLD_x", "INDHOLD_y"]]
df_top5_filtered["PCT"] = (df_top5_filtered["INDHOLD_y"]/df_top5_filtered["INDHOLD_x"]*100)

print(df_top5_filtered)


# 5.3:
url_total_cph = "https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=Value&delimiter=Semicolon&OMR%C3%85DE=101&CIVILSTAND=U%2CG%2CE%2CF&Tid=2008K4%2C2009K4%2C2010K4%2C2011K4%2C2012K4%2C2013K4%2C2014K4%2C2015K4%2C2016K4%2C2017K4%2C2018K4%2C2019K4%2C2020K4"

df_total_cph = pd.read_csv(url_total_cph, sep=';')

plot_total_cph = df_total_cph.pivot(index='TID', columns='CIVILSTAND', values='INDHOLD')

def show_cph():
    plot_total_cph.plot(kind="bar")
    plt.xlabel('Year')
    plt.ylabel('Total')
    plt.show()

#show_cph()


# 5.4:
url_2020 = "https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=Value&delimiter=Semicolon&OMR%C3%85DE=000&CIVILSTAND=U%2CG&Tid=2020K4&ALDER=*"

df_2020 = pd.read_csv(url_2020, sep=';')

#print(df_2020)

df_total_married = df_2020[(df_2020['CIVILSTAND'] != 'Ugift') & (df_2020['ALDER'] != 'I alt')].reset_index(drop='True')
df_total_unmarried = df_2020[(df_2020['CIVILSTAND'] == 'Ugift') & (df_2020['ALDER'] != 'I alt')].reset_index(drop='True')

def show_2020():
    ax = df_total_married.plot()
    df_total_unmarried.plot(ax=ax)
    plt.xlabel('Age')
    plt.ylabel('Total')
    plt.legend(["Married", "Unmarried"])
    plt.show()

show_2020()

