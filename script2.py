file_city = open('test.txt', 'r', encoding='utf8')
city_list = file_city.readlines()
file_city.close()

file_city2 = open('checked-cities.txt', 'w', encoding='utf8')
for city in city_list:
    file_city2.write(f'{city.strip()}\n')
file_city2.close()
