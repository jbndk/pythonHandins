import numpy as np
import pandas as pd
import requests
import zipfile

#url = 'http://api.worldbank.org/v2/en/country/DNK;URY'
#response = requests.get(url, params={'downloadformat': 'csv'})
#url = 'http://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.KT?downloadformat=csv'
#response = requests.get(url)

#print(response.headers)

# get the filename
#fname = response.headers['Content-Disposition'].split('=')[1]
#fname = 'C:\\Users\\Jonas\\Desktop\\Sem4\\Python\\docker_notebooks\\notebooks\\data\\'+fname
# write content to file (zip file writing bytes)
#if response.ok:  # status_code == 200:
#    with open(fname, 'wb') as f:
#        f.write(response.content)
#print('-----------------')
#print('Downloaded {}'.format(fname))

# extract content of zip file in current folder
# zipfile.ZipFile(fname, 'r').extractall('C:\\Users\\Jonas\\Desktop\\Sem4\\Python\\docker_notebooks\\notebooks\\data\\')


data = pd.read_csv('C:\\Users\\Jonas\\Desktop\\Sem4\\Python\\docker_notebooks\\notebooks\\data\\API_EN.ATM.CO2E.KT_DS2_en_csv_v2_1345584.csv', skiprows=4)
columns_names = data.columns
#print('column names:\n',list(columns_names),'\n\n')
countries = data['Country Name']
#print('{} countries are in the dataset.'.format(len(countries)),'\n')
#print('countries are of data type: ',type(countries),'\n')
#print(list(countries))
#data

data = data.set_index("Country Name")
co2_data = data["2014"]

print(co2_data)

sorted_co2_data = co2_data.sort_values(ascending=False)
print(sorted_co2_data[:10])