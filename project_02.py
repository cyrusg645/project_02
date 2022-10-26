### json ###

import json
rick_and_morty_dataset = open('/Users/cyrus/Documents/GitHub/cyrusg645.github.io/rick_and_morty_dataset.json')
reader = rick_and_morty_dataset.read()
rick_and_morty_dataset_json = json.loads(reader)

count_airdate = {'2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0, '2021': 0, '2022': 0}
for i in rick_and_morty_dataset_json['_embedded']['episodes']: 

    for x in count_airdate:
        if x in i['airdate']:
            count_airdate[x] += 1
terms = list(count_airdate.keys())
counts = list(count_airdate.values())
print('count_airdate=', count_airdate)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(terms, counts)
plt.title('Number of Rick and Morty Episodes Produced Each Year (2013-2022)')
plt.xlabel('Year')
plt.ylabel('Number of Episodes')
plt.legend(['Episodes'])
plt.show()

### csv ###

import csv
populationgrowth = open('/Users/cyrus/Documents/GitHub/cyrusg645.github.io/population.csv')
populationgrowth_read = csv.reader(populationgrowth)
populationgrowth_list = list(populationgrowth_read)
china_data = populationgrowth_list[45][5:-1]
united_states_data = populationgrowth_list[256][5:-1]
years_data = populationgrowth_list[4][5:-1]

china_data_float = []
for rate in china_data:
    china_data_float.append(float(rate))
print(china_data_float)

united_states_data_float = []
for rate in united_states_data:
    united_states_data_float.append(float(rate))
print(united_states_data_float)

years_data_int = []
for year in years_data:
    years_data_int.append(int(year))
print(years_data_int)

import matplotlib.pyplot as plt
plt.plot(years_data_int, china_data_float)
plt.plot(years_data_int,united_states_data_float)
plt.title('Population Growth Rate over Time (1960-2021)')
plt.xlabel('Year')
plt.ylabel('Population Growth Rate')
plt.legend(['China'], ['United States'])
plt.show()





