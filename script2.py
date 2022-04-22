file_city = open('city-list.txt', 'r', encoding='utf8')
city_list = file_city.readlines()
file_city.close()

file_city2 = open('checked-cities.txt', 'w', encoding='utf8')
for city in city_list:
    file_city2.write(f'{city}\n')