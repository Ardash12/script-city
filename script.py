import requests

data = {
    "name": "111"
}

file_city = open('city-list.txt', 'r', encoding='utf8')
city_list = file_city.readlines()
file_city.close()
print(city_list[0][0:-1])
file_check = open('checked-cities.txt', 'w', encoding='utf8')
for city in city_list:
    r = requests.post('http://127.0.0.1:8000/city/', data={
        'name': city[0:-1]
    })
    print(r.text)
    file_check.write(f'{city[0:-1]} {r.text}\n')
file_check.close()
# print(r.status_code)
# print(r.text)
