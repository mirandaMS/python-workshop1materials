# Extracting a list of the top 50 U.S. cities by population
# Data from http://www.politifact.com/largestcities/
# Author: Miranda So
# Date: Feb. 22, 2018

citiesFile = 'top50cities.txt'
citiesList = 'top50cities_cleaned.txt'

with open(citiesFile, 'r') as cities:
    with open(citiesList, 'w') as cleaned:
        for i in cities:
            if i[0] != '"':
                pass
            else:
                firstSpace = i.find(' ')
                lastSpace = i.rfind(' ')
                city = i[firstSpace+1:lastSpace]
                if ',' in city:    # some city names in format "city, state"
                    comma = city.find(',')
                    just_city = city[:comma]    # removing state names
                    cleaned.write(just_city)
                else:
                    cleaned.write(city)
                cleaned.write('\n')
            
print('Cleaned city file has been created.')       

# Creating a list from those cities

l = []
with open(citiesList, 'r') as cleaned:
    for i in cleaned:
        i = i.replace('\n','')
        l.append(i)

print(l)
